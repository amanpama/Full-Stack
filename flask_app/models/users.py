from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("usersCR").query_db(query)

        users = []
        for result in results:
            one_instance = cls(result)
            users.append(one_instance)
        return users

    @classmethod
    def save(cls,data):
        query ="INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW(), NOW());"
        users_id = connectToMySQL("usersCR").query_db(query,data)

        return users_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * from users WHERE id = %(id)s;"
        results = connectToMySQL("usersCR").query_db(query,data)
        single_user = cls(results[0])
        return single_user

    @classmethod
    def edit(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return connectToMySQL("usersCR").query_db(query,data)

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id= %(id)s;"
        return connectToMySQL("usersCR").query_db(query,data)