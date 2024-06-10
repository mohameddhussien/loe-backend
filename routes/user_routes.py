from flask import Blueprint
from controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/users", methods=["GET"])
def handle_get_users():
    userController = UserController()
    return userController.get_users()

@user_bp.route("/login", methods=["POST"])
def handle_login():
    userController = UserController()
    return userController.login()

@user_bp.route("/get-user-by-token", methods=["POST"])
def handle_get_user_data():
    userController = UserController()
    return userController.get_user_data()

@user_bp.route("/register", methods=["POST"])
def handle_register():
    userController = UserController()
    return userController.register()

