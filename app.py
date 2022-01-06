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
    decks = list(mongo.db.decks.find())
    return render_template("index.html", decks=decks)


@app.route("/all_decks/<username>")
def all_decks(username):
    if session["user"]:
        # Find the session user's username from database.
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        decks = mongo.db.decks.find()
        user = mongo.db.users.find_one(
                    {"username": session["user"]})
        user_id = str(ObjectId(user.get("_id")))

        # Find all decks and all decks created by session user.

        return render_template(
            "all_decks.html", username=username, decks=decks, user_id=user_id)

    return redirect(url_for("index"))


@app.route("/create_an_account", methods=["GET", "POST"])
def create_an_account():
    # Prevents an already logged in user from creating a new account.
    if session.get("user") is None:
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
                "is_super_admin": False,
                "join_date": date.strftime("%-d-%b-%Y"),
                "loved_decks": []
            }
            mongo.db.users.insert_one(new_user)

            # Put the user into a 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("You've created your account!")
            return redirect(url_for("my_decks", username=session["user"]))

        return render_template("create_an_account.html")

    else:
        flash("You already have an account!")
        return redirect(url_for("my_decks", username=session["user"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user") is None:
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
                        session["super_admin"] = existing_user.get("is_super_admin")
                        user_id = str(ObjectId(existing_user.get("_id")))
                        session["id"] = user_id
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

    else:
        flash("You've already logged in!")
        return redirect(url_for("my_decks", username=session["user"]))


@app.route("/my_decks/<username>", methods=["GET", "POST"])
def my_decks(username):
    # Find the session user's username from database.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = mongo.db.users.find_one(
            {"username": session["user"]})
    user_id = str(ObjectId(user.get("_id")))

    user_decks = list(mongo.db.decks.find({"deck_created_by": username}))
    user_loved_decks = mongo.db.decks.find({"deck_loved_by": user_id})

    if session["user"]:
        return render_template(
            "my_decks.html", username=username, user_decks=user_decks, user_loved_decks=user_loved_decks)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("Log Out Successful")
    session.clear()
    return redirect(url_for("login"))


@app.route("/create_deck", methods=["GET", "POST"])
def create_deck():
    if session["user"]:
        # The following code is used to ensure that a user will have a 'session["id"]'
        #  even if they have just created their account, and have
        #  not been granted a 'session["id"]' through login.
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        user_id = str(ObjectId(user.get("_id")))
        session["id"] = user_id

        if request.method == "POST":

            deck = {
                "deck_name": request.form.get("deck_name"),
                "deck_language": request.form.get("deck_language"),
                "deck_level": request.form.get("deck_level"),
                "deck_description": request.form.get("deck_description"),
                "deck_created_by": session["user"],
                "deck_created_by_id": session["id"],
                "deck_loved_by": [],
                "deck_love_counter": 0,
                "deck_report_counter": 0,
                "deck_times_played": 0,
            }
            
            deck["deck_card_fronts"] = []
            deck["deck_card_backs"] = []
            
            max_cards = 30

            for i in range(max_cards):

                front_input_name = f"{i}_card_front"
                back_input_name = f"{i}_card_back"

                front_input_value = request.form.get(front_input_name)
                back_input_value = request.form.get(back_input_name)
                
                if front_input_value != "" and front_input_value is not None and back_input_value != "" and back_input_value is not None:
                    deck['deck_card_fronts'].append(
                        front_input_value)
                    deck['deck_card_backs'].append(
                        back_input_value)

                else:
                    pass

            mongo.db.decks.insert_one(deck)
            flash("Deck Created!")
            return redirect(url_for("my_decks", username=session["user"]))

        return render_template("create_deck.html")


@app.route("/edit_deck/<deck_id>", methods=["GET", "POST"])
def edit_deck(deck_id):
    if session["user"]:
        deck = mongo.db.decks.find_one({"_id": ObjectId(deck_id)})

        if request.method == "POST":
            mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$set": {
                "deck_name": request.form.get("deck_name"),
                "deck_language": request.form.get("deck_language"),
                "deck_level": request.form.get("deck_level"),
                "deck_description": request.form.get("deck_description"),
            }})
            deck["deck_card_fronts"] = []
            deck["deck_card_backs"] = []
            
            max_cards = 30

            for i in range(max_cards):

                front_input_name = f"{i}_card_front"
                back_input_name = f"{i}_card_back"

                front_input_value = request.form.get(front_input_name)
                back_input_value = request.form.get(back_input_name)
                
                if front_input_value != "" and front_input_value is not None and back_input_value != "" and back_input_value is not None:
                    deck['deck_card_fronts'].append(
                        front_input_value)
                    deck['deck_card_backs'].append(
                        back_input_value)
                
                else:
                    pass
                mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$set": {
                    "deck_card_fronts": deck['deck_card_fronts'],
                    "deck_card_backs": deck['deck_card_backs'],
                    }})

            flash("Deck Changes Saved!")
            
        return render_template("edit_deck.html", deck=deck)


@app.route("/delete_cards/<deck_id>")
def delete_cards(deck_id):
    
    if session["user"]:

        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$set": {
                    "deck_card_fronts": ["Add your word here!"],
                    "deck_card_backs": ["Add the translation here!"],
                    }})
        flash("Cards Deleted")
        


        return redirect(url_for("edit_deck", deck_id=deck_id))


@app.route("/play_deck/<deck_id>")
def play_deck(deck_id):
    if session["user"]:

        user = mongo.db.users.find_one(
                {"username": session["user"]})
        deck = mongo.db.decks.find_one({"_id": ObjectId(deck_id)})
        user_id = str(ObjectId(user.get("_id")))

        return render_template(
            "play_deck.html", deck=deck, deck_id=deck_id, user_id=user_id)


@app.route("/play_deck_anonymous/<deck_id>")
def play_deck_anonymous(deck_id):

    deck = mongo.db.decks.find_one({"_id": ObjectId(deck_id)})
    return render_template(
        "play_deck_anonymous.html", deck=deck, deck_id=deck_id)


@app.route("/love_deck/<deck_id>")
def love_deck(deck_id):
    if session["user"]:
        # The following code is used to ensure
        # that a user will have a 'session["id"]'
        # even if they have just created their account, and have
        # not been granted a 'session["id"]' through login.
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        user_id = str(ObjectId(user.get("_id")))
        session["id"] = user_id

        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$push": {
            "deck_loved_by": user_id}})
        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$inc": {"deck_love_counter": 1}})

        return redirect(url_for("play_deck", deck_id=deck_id))


@app.route("/unlove_deck/<deck_id>")
def unlove_deck(deck_id):
    if session["user"]:
        # The following code is used to ensure
        # that a user will have a 'session["id"]'
        # even if they have just created their account, and have
        # not been granted a 'session["id"]' through login.
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        user_id = str(ObjectId(user.get("_id")))
        session["id"] = user_id

        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$pull": {
            "deck_loved_by": user_id}})
        mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$inc": {"deck_love_counter": -1}})

        return redirect(url_for("play_deck", deck_id=deck_id))


@app.route("/delete_deck/<deck_id>")
def delete_deck(deck_id):
    if session["user"]:

        mongo.db.decks.remove({"_id": ObjectId(deck_id)})
        flash("Deck Deleted")
        return redirect(url_for("my_decks", username=session["user"]))


@app.route("/user_management")
def user_management():

    if session["admin"]:

        users = list(mongo.db.users.find().sort("username"))

        return render_template("user_management.html", users=users)


@app.route("/admin_delete_user/<user_id>")
def admin_delete_user(user_id):
    if session["admin"]:

        users = list(mongo.db.users.find())
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        mongo.db.decks.remove({"deck_created_by_id": user_id})
        
        flash("User and Decks Deleted")

        return redirect(url_for("user_management", users=users))


@app.route("/admin_promote_user/<user_id>")
def admin_promote_user(user_id):
    if session["super_admin"]:

        users = list(mongo.db.users.find())
        mongo.db.users.update({"_id": ObjectId(user_id)}, {"$set": {
                "is_admin": True}})
        flash("User Promoted!")

        return redirect(url_for("user_management", users=users))


@app.route("/admin_demote_user/<user_id>")
def admin_demote_user(user_id):
    if session["super_admin"]:

        users = list(mongo.db.users.find())
        mongo.db.users.update({"_id": ObjectId(user_id)}, {"$set": {
                "is_admin": False}})
        flash("User Demoted!")

        return redirect(url_for("user_management", users=users))


@app.route("/create_new_admin", methods=["GET", "POST"])
def create_new_admin():
    if session["super_admin"]:

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
                "is_super_admin": False,
                "join_date": date.strftime("%-d-%b-%Y"),
                "my_decks": [],
            }
            mongo.db.users.insert_one(new_user)

            flash("New Admin Created")
            return redirect(url_for("user_management"))

        return render_template("create_new_admin.html")


@app.route("/deck_management")
def deck_management():

    if session["admin"]:

        decks = list(mongo.db.decks.find().sort("deck_created_by"))
        return render_template("deck_management.html", decks=decks)


@app.route("/admin_delete_deck/<deck_id>")
def admin_delete_deck(deck_id):
    if session["admin"]:

        mongo.db.decks.remove({"_id": ObjectId(deck_id)})
        flash("Deck Deleted")
        
        return redirect(url_for("deck_management"))


@app.route("/admin_view_decks/<user_id>")
def admin_view_decks(user_id):
    if session["admin"]:

        user_decks = list(mongo.db.decks.find({"deck_created_by_id": user_id}))
        return render_template("admin_view_decks.html", user_id=user_id, user_decks=user_decks)


@app.route("/create_report/<deck_id>", methods=["GET", "POST"])
def create_report(deck_id):
    if session["user"]:
        # The following code is used to ensure that a user will have a 'session["id"]'
        #  even if they have just created their account, and have
        #  not been granted a 'session["id"]' through login.
        date = datetime.now().date()
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        deck = mongo.db.decks.find_one(
            {"_id": ObjectId(deck_id)})

        user_id = str(ObjectId(user.get("_id")))
        session["id"] = user_id

        if request.method == "POST":

            report = {
                "deck_name": deck.get("deck_name"),
                "deck_id": deck.get("_id"),
                "reported_by": user.get("username"),
                "report_date": date.strftime("%-d-%b-%Y"),
                "report_check_1": request.form.get("report_check_1"),
                "report_check_2": request.form.get("report_check_2"),
                "report_check_3": request.form.get("report_check_3"),
                "report_check_4": request.form.get("report_check_4"),
                "report_check_5": request.form.get("report_check_5"),
                "report_check_6": request.form.get("report_check_6"),
                "report_details": request.form.get("report_details"),
                "report_closed": False
            }

            mongo.db.decks.update({"_id": ObjectId(deck_id)}, {"$inc": {"deck_report_counter": 1}})
            mongo.db.reports.insert_one(report)
            flash("Thanks, your report has been sumbitted!")
            return redirect(url_for("my_decks", username=session["user"]))

        return render_template("create_report.html", deck=deck)


@app.route("/report_management")
def report_management():

    if session["admin"]:

        reports = mongo.db.reports.find({"report_closed": False}).sort("report_date")
        return render_template("report_management.html", reports=reports)


@app.route("/report_archive")
def report_archive():

    if session["admin"]:

        reports = mongo.db.reports.find({"report_closed": True}).sort("report_date")
        return render_template("report_archive.html", reports=reports)


@app.route("/admin_close_report/<report_id>")
def admin_close_report(report_id):
    if session["admin"]:

        mongo.db.reports.update({"_id": ObjectId(report_id)}, {"$set": {
                "report_closed": True}})
        flash("Report Closed")

        return redirect(url_for("report_management"))


@app.route("/admin_reopen_report/<report_id>")
def admin_reopen_report(report_id):
    if session["admin"]:

        mongo.db.reports.update({"_id": ObjectId(report_id)}, {"$set": {
                "report_closed": False}})
        flash("Report Reopened")

        return redirect(url_for("report_archive"))


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