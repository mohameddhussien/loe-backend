from models.db import Database

class UserModel:
    def __init__(self, db: Database):
        self.db = db
        
    def get_all_users(self):
        users = self.db.call_stored_procedure("GetAllClientUsers")
        return users

    def get_user_by_credentials(self, email, password):
        user = self.db.call_stored_procedure("GetPerson", (email, password))
        return user

    def get_user_by_id(self, user_id):
        user = self.db.call_stored_procedure("GetPersonById", (user_id,))
        return user

    def insert_user(self, data):
        return self.db.call_stored_procedure("InsertUser", data)