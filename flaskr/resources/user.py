import json

from flask import make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.mongo_serve import conn_mongo_main


class UserResource(Resource):
    def __init__(self):
        super().__init__()
        db_instance = conn_mongo_main()
        self.user_instance = db_instance.user
        self.user_history = db_instance.history

    def post(self):
        _user = request.json.get("_user")
        _pwd = request.json.get("_pwd")
        if self.user_instance.find_one({"user": _user}):
            return make_response({"message": "Username already exists"}, 400)

        self.user_instance.insert_one({"user": _user, "pwd": _pwd})
        return make_response({"message": "User create"}, 200)

    @jwt_required()
    def get(self):
        user = self.user_instance.find()
        user_list = []
        for _user in user:
            user_list.append(_user["user"])
        user_json = json.dumps(user_list)
        return make_response(user_json)
