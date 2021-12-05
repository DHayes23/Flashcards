import os
from flask import (
     Flask, flash, render_template,
      redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
            "my_decks": [],
            "loved_decks": []
        }
        mongo.db.users.insert_one(new_user)

        # Put the user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You've created your account!")
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
                    session["user"] = request.form.get("username").lower()
                    # flash(f"Thanks {request.form.get('username')}")
                    flash("You've been logged in!")
            else:
                # Invalid password match
                flash("Please enter a valid Username and Password")
                return redirect(url_for("login"))

        else:
            # Non-existant username
            flash("Please enter a valid Username and Password")
            return redirect(url_for("login"))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
