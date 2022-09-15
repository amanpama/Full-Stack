from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.users import User
from flask_app.models.dojos import Dojo

@app.route("/")
def index():
    all_dojos=Dojo.get_all()
    # print(all_dojos)
    return render_template("index.html",all_dojos=all_dojos)

@app.route("/addninja")
def addninja():
    all_dojos=Dojo.get_all()
    return render_template("AddNinjaPage.html",all_dojos=all_dojos)

@app.route("/viewusers")
def viewusers():
    all_users = User.get_all()
    print(all_users)
    return render_template("viewusers.html", all_users=all_users )

@app.route("/viewusers/<int:id>")
def viewninjas(id):
    data ={
        "id": id
    }
    single_dojo = Dojo.get_one(data)
    all_ninjas = User.get_all(data)
    return render_template("viewusers.html",single_dojo=single_dojo, all_ninjas=all_ninjas)

@app.route("/addninja/submit",methods=["post"])
def submit_ninja():
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojos_id": request.form["dojos_id"]
    }

    User.save(data)

    return redirect("/")

@app.route("/addDojo",methods=["post"])
def submit_dojo():
    
    print(request.form)
    data = {
        "name": request.form["name"]
    }
    # print("yo")

    Dojo.save(data)

    return redirect("/")