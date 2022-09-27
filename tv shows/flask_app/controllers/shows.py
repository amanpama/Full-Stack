from re import L
from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User
from flask_app.models.displayshows import Show

@app.route("/shows")
def success():
    if "logged_id" not in session:
        return redirect("/")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    all_shows = Show.get_all()

    return render_template("main.html", logged_user=logged_user, all_shows=all_shows)

@app.route("/shows/new")
def create_shows_page():
    if "logged_id" not in session:
        return redirect("/")
    return render_template("create.html")

@app.route("/shows/submit", methods=["post"])
def submit_team():
    if "logged_id" not in session:
        return redirect("/")
    # print("trying to sumbit recipe")

    data ={
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "users_id": session["logged_id"],
    }
    if not Show.validate(data):
        return redirect("/shows/new")
    Show.save(data)

    return redirect("/shows")

@app.route("/shows/<int:id>/edit")
def edit_show_page(id):
    if "logged_id" not in session:
        return redirect("/")

    data = {
        "id" :id
    }

    one_show = Show.get_one(data)

    return render_template("edit.html", one_show=one_show)

@app.route("/shows/submit_edit",methods=["post"])
def sumbit_edit():
    if "logged_id" not in session:
        return redirect("/")

    data ={
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "id": request.form ["show_id"]
    }

    Show.edit_show(data)

    return redirect("/shows")

@app.route("/shows/<int:id>/show")
def show_show(id):
    if "logged_id" not in session:
        return redirect("/")
    data={
        "id" : id
    }
    user_data = {
        "id": session["logged_id"]
    }
    logged_user=User.find_one_by_id(user_data)
    single_show = Show.get_one(data)
    print(f"trying to find user with id: {id}")
    return render_template("show.html", single_show=single_show, logged_user=logged_user)   

@app.route("/users/<int:id>/delete")
def delete_user(id):
    if "logged_id" not in session:
        return redirect("/")
    print(f"trying to delete user with id: {id}")
    data = {
    "id": id
    }
    Show.delete_user(data)
    return redirect("/shows")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")