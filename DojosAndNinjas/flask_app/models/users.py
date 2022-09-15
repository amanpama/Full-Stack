from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM ninjas WHERE dojos_id=%(id)s"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

        ninjas = []
        for result in results:
            one_instance = cls(result)
            ninjas.append(one_instance)

        print(ninjas)
        return ninjas

    @classmethod
    def save(cls,data):
        query ="INSERT INTO ninjas (first_name,last_name,created_at,updated_at,age,dojos_id) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW(), %(age)s, %(dojos_id)s);"
        ninjas_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

        return ninjas_id 
    