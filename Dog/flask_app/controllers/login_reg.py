from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.users import User
# from flask_app.models.displaydogs import Dog

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route("/login")
def index():
    return render_template("login.html")

@app.route("/register", methods=["post"])
def register_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"],
    }
    this_user = User.find_one_by_email(data)

    if this_user:
        flash("Email is already in use!")
        return redirect("/login")

    if not User.validate(data):
        # print("not valid")
        return redirect("/login")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data["password"] = pw_hash
    # print(f"password: {request.form['password']}")
    # print(f"hashed password: {pw_hash}")

    user_id = User.save(data)
    session["logged_id"] = user_id


    return redirect("/login")

@app.route("/login",methods=["post"])
def login_user():
    data = {
        "email": request.form["email"]
    }

    this_user = User.find_one_by_email(data)

    if not this_user:
        flash("Invalid email/password. Please try again")
        return redirect("/login")

    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid email/password. Please try again")
        return redirect("/login")

    session["logged_id"] = this_user.id

    # print("sucessful login")

    return redirect("/")