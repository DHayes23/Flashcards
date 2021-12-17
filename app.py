import os
from flask import (
     Flask, flash, render_template,
      redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    decks = mongo.db.decks.find()
    return render_template("index.html", decks=decks)


@app.route("/create_an_account", methods=["GET", "POST"])
def create_an_account():
    if request.method == "POST":
        date = datetime.now().date()
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry, that username is taken!")
            return redirect(url_for("create_an_account"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": False,
            "join_date": date.strftime("%-d-%b-%Y"),
            "my_decks": [],
            "loved_decks": []
        }
        mongo.db.users.insert_one(new_user)

        # Put the user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You've created your account!")
        return redirect(url_for("my_decks", username=session["user"]))

    return render_template("create_an_account.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username is in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Confirm matching password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = existing_user.get("username")
                    # The following session is granted to admins,
                    #  providing special access
                    session["admin"] = existing_user.get("is_admin")
                    user_id = str(ObjectId(existing_user.get("_id")))
                    session["id"] = user_id
                    # flash(f"Thanks {request.form.get('username')}")
                    flash("You've been logged in!")
                    return redirect(url_for(
                        "my_decks", username=session["user"]))
            else:
                # Invalid password match
                flash("Please enter a valid Username and Password")
                return redirect(url_for("login"))

        else:
            # Non-existant username
            flash("Please enter a valid Username and Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_decks/<username>", methods=["GET", "POST"])
def my_decks(username):
    # Find the session user's username from database.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    user_decks = mongo.db.decks.find({"deck_created_by": username})

    if session["user"]:
        return render_template("my_decks.html", username=username, user_decks=user_decks)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("Log Out Successful")
    session.clear()
    return redirect(url_for("login"))


@app.route("/create_deck", methods=["GET", "POST"])
def create_deck():
    if request.method == "POST":
        deck = {
            "deck_name": request.form.get("deck_name"),
            "deck_language": request.form.get("deck_language"),
            "deck_level": request.form.get("deck_level"),
            "deck_description": request.form.get("deck_description"),
            "deck_card_contents": [],
            "deck_created_by": session["user"],
            "deck_created_by_id": session["id"],
            "deck_love_counter": 0,
            "deck_times_played": 0,
            "deck_number_of_cards": 0,
        }
        mongo.db.decks.insert_one(deck)
        flash("Deck Changes Saved!")
        return redirect(url_for("my_decks", username=session["user"]))

    return render_template("create_deck.html")


@app.route("/edit_deck/<deck_id>", methods=["GET", "POST"])
def edit_deck(deck_id):
    if request.method == "POST":
        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$set": {
            "deck_name": request.form.get("deck_name"),
            "deck_language": request.form.get("deck_language"),
            "deck_level": request.form.get("deck_level"),
            "deck_description": request.form.get("deck_description"),
        }})
        flash("Deck Changes Saved!")

    deck = mongo.db.decks.find_one({"_id": ObjectId(deck_id)})
    return render_template("edit_deck.html", deck=deck)


@app.route("/delete_deck/<deck_id>")
def delete_deck(deck_id):
    mongo.db.decks.remove({"_id": ObjectId(deck_id)})
    flash("Deck Deleted")
    return redirect(url_for("my_decks", username=session["user"]))


@app.route("/user_management")
def user_management():
    users = list(mongo.db.users.find())

    return render_template("user_management.html", users=users)


@app.route("/admin_delete_user/<user_id>")
def admin_delete_user(user_id):
    users = list(mongo.db.users.find())
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Deleted")

    return redirect(url_for("user_management", users=users))


@app.route("/create_new_admin", methods=["GET", "POST"])
def create_new_admin():
    if request.method == "POST":
        date = datetime.now().date()
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry, that username is taken!")
            return redirect(url_for("create_new_admin"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": True,
            "join_date": date.strftime("%-d-%b-%Y"),
            "my_decks": [],
        }
        mongo.db.users.insert_one(new_user)

        flash("New Admin Created")
        return redirect(url_for("user_management"))

    return render_template("create_new_admin.html")


@app.errorhandler(404)
def error_404(e):

    return render_template('404_error.html')


@app.errorhandler(500)
def internal_server_error(e):

    return render_template('500_error.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
