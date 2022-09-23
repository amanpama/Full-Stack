from re import L
from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User
from flask_app.models.displaydogs import Dog

@app.route("/")
def mainpage():
    return render_template("MainPage.html")

@app.route("/PostAdoption")
def postadoptionpage():
    return render_template("PostAdoption.html")

@app.route("/about")
def aboutme():
    return render_template("aboutme.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["post"])
def submit_dog():

    if "logged_id" not in session:
        return redirect("/login")

    data ={
        "name": request.form["name"],
        "breed": request.form["breed"],
        "age": request.form["age"],
        "weight": request.form["weight"],
        "sex": request.form["sex"],
        "birthday": request.form["birthday"],
        "personality": request.form["personality"],
        "users_id": session["logged_id"],
    }
    if not Dog.validate(data):
        return redirect("/")
    Dog.save(data)

    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")