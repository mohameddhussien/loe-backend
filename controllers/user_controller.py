from flask import jsonify, request, g
from models.user_model import UserModel
from utils.jwt_utils import generate_token, decode_token
from models.db import Database

class UserController:
    def __init__(self):
        self.db: Database = g.db

    def get_users(self):
        userModel = UserModel(self.db)
        users = userModel.get_all_users()
        return jsonify(users if users else [])

    def login(self):
        email = request.json.get("email")
        password = request.json.get("password")
        
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        userModel = UserModel(self.db)
        user = userModel.get_user_by_credentials(email, password)
        if user:
            token = generate_token(user)
            return jsonify({"token": token, "user": user}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    def get_user_data(self):
        token = request.json.get("token")
        if not token:
            return jsonify({"error": "Token is required"}), 400

        decoded_data = decode_token(token)
        if "error" in decoded_data:
            return jsonify(decoded_data), 401

        user_id = decoded_data.get("data").split("-")[0]
        userModel = UserModel(self.db)
        user = userModel.get_user_by_id(user_id)
        if user:
            return jsonify({"user": user}), 200
        else:
            return jsonify({"error": "User not found"}), 404
        
    def register(self):
        # Your implementation for user registration
        pass
