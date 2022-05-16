from flask import Blueprint, Response, json, request

from service.user_service import UserService

app_user = Blueprint("app_user", __name__)
user_service = UserService()

@app_user.route("/user")
def get_user():
    return user_service.list_users()
