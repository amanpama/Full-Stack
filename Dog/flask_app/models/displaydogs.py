from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.users import User

class Dog:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.breed = data["breed"]
        self.age = data["age"]
        self.weight = data["weight"]
        self.sex = data["sex"]
        self.birthday = data["birthday"]
        self.personality = data["personality"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["users_id"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows JOIN users ON shows.users_id = users.id;"

        results = connectToMySQL("dogs").query_db(query)
        # print(results)
        dogs = []

        for row_from_db in results:
            one_dog = cls(row_from_db)

            dogs.append(one_dog)

        return dogs

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dog (name,breed,age,weight,sex,birthday,personality,created_at,updated_at,users_id) VALUES (%(name)s,%(breed)s,%(age)s,%(weight)s,%(sex)s,%(birthday)s,%(personality)s,NOW(),NOW(),%(users_id)s);"
        
        dog_id = connectToMySQL("dogs").query_db(query,data)
        
        return dog_id

    @staticmethod
    def validate (data):
        is_valid = True
        if len(data["name"]) < 1:
            flash ("Name must be atleast 1 character")
            is_valid = False
        if len(data["breed"]) < 1:
            flash ("Breed must be atleast 1 character")
            is_valid = False
        if len(data["age"]) < 1:
            flash ("Description must be atleast 1 character")
            is_valid = False
        if len(data["weight"]) < 1:
            flash ("Weight must be atleast 1 character")
            is_valid = False
        if len(data["personality"]) < 1:
            flash ("Personality description must be atleast 4 characters")
            is_valid = False
        return is_valid