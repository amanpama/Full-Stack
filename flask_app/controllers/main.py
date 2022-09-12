from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.users import User

@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users = all_users)

@app.route("/userpage")
def create_form():
    return render_template("userform.html")

@app.route("/userpage/submit", methods=["post"])
def submit_user():
    print(request.form)

    data = {
        "first_name": request.form ["first_name"],
        "last_name": request.form ["last_name"],
        "email": request.form ["email"],
    }

    User.save(data)

    return redirect("/")

@app.route("/users/<int:id>")
def single_user_page(id):
    data={
        "id" : id
    }
    single_user = User.get_one(data)
    print(f"trying to find user with id: {id}")
    return render_template("single_user.html", single_user=single_user) 

@app.route("/users/<int:id>/edit_page")
def edit_user_page(id):
    data={
        "id" : id
    }
    single_user = User.get_one(data)
    return render_template("edit.html",single_user=single_user )

@app.route("/users/<int:id>/submit_edit", methods=["post"])
def submit_edit(id):
    data = {
        "id": id,
        "first_name": request.form ["first_name"],
        "last_name": request.form ["last_name"],
        "email": request.form ["email"]
    }
    User.edit(data)
    print(f"trying to edit user # {id}")
    return redirect("/")

@app.route("/users/<int:id>/delete")
def delete_user(id):
    print(f"trying to delete user with id: {id}")
    data = {
    "id": id
    }
    User.delete_user(data)
    return redirect("/userpage")