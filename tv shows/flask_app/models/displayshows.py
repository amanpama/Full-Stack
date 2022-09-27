from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.users import User

class Show:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.description = data["description"]
        self.user_id = data["users_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.poster = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows JOIN users ON shows.users_id = users.id;"

        results = connectToMySQL("exam").query_db(query)
        # print(results)
        shows = []

        for row_from_db in results:
            one_show = cls(row_from_db)

            poster_data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"],
            }
            one_show.poster = User(poster_data) 

            shows.append(one_show)

        return shows

    @classmethod
    def save(cls,data):
        query = "INSERT INTO shows (title,network,release_date,description,created_at,updated_at,users_id) VALUES (%(title)s,%(network)s,%(release_date)s,%(description)s,NOW(),NOW(),%(users_id)s);"
        
        show_id = connectToMySQL("exam").query_db(query,data)
        
        return show_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM shows WHERE id=%(id)s;"

        results = connectToMySQL("exam").query_db(query,data)

        one_instance = cls(results[0])
        return one_instance

    @classmethod
    def edit_show(cls,data):
        query="UPDATE shows SET title=%(title)s,network=%(network)s,release_date=%(release_date)s,description=%(description)s,updated_at=NOW() WHERE id=%(id)s;"        
        connectToMySQL("exam").query_db(query,data)
        return

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM shows WHERE id= %(id)s;"
        return connectToMySQL("exam").query_db(query,data)

    @staticmethod
    def validate (data):
        is_valid = True
        if len(data["title"]) < 3:
            flash ("Title must be atleast 3 characters")
            is_valid = False
        if len(data["network"]) < 3:
            flash ("Network must be atleast 3 characters")
            is_valid = False
        if len(data["description"]) < 3:
            flash ("Description must be atleast 3 characters")
            is_valid = False
        return is_valid