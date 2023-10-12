import json

from flask import make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.mongo_serve import db_instance


class UserResource(Resource):
    def __init__(self):
        super().__init__()
        self.users_instance = db_instance.user

    def post(self):
        _user = request.json.get("_user")
        _pwd = request.json.get("_pwd")
        if self.users_instance.find_one({"user": _user}):
            return make_response({"message": "Username already exists"}, 400)

        self.users_instance.insert_one(
            {"user": _user, "pwd": _pwd, "version_terms": ""}
        )

        return make_response({"message": "User create"}, 200)

    @jwt_required()
    def get(self):
        user = self.users_instance.find()
        user_list = []
        for _user in user:
            user_list.append(_user["user"])
        user_json = json.dumps(user_list)
        return make_response(user_json)
