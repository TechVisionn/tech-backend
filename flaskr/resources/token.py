from flask import make_response, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Resource

from flaskr.db.mongo_serve import db_instance
from flaskr.security import ACCESS_EXPIRES


class TokenResource(Resource):
    def __init__(self):
        super().__init__()
        self.token_instance = db_instance.token
        self.user_instance = db_instance.user
        self.term_instance = db_instance.Term

    def post(self):
        _user = request.json.get("_user")
        _pwd = request.json.get("_pwd")
        _term = request.json.get("_term")

        user = self.user_instance.find_one({"user": _user, "pwd": _pwd})
        if user is None:
            return make_response({"message": "Invalid username or password"})

        latest_term = self.term_instance.find_one(sort=[("version", -1)])
        print(latest_term)
        if latest_term != user["version_term"] or not latest_term:
            if _term is None or  _term is False:
                return make_response({"message": "User needs to update terms"})
            else:
                self.user_instance.update_one(
                    {"_id": user["_id"]},
                    {"$set": {"version_term": latest_term}},
                )

        # create a new token with the user id inside
        access_token = create_access_token(identity=str(user["_id"]))
        refresh_token = create_refresh_token(str(user["_id"]))

        return make_response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "uid": str(user["_id"]),
            },
            201,
        )

    @jwt_required()
    def delete(self, **kwargs):
        current_user_id = get_jwt_identity()
        jti = get_jwt()["jti"]
        revoked_token = {"jti": jti, "user_id": current_user_id}
        self.token_instance.insert_one(revoked_token)

        return make_response({"message": "Access token revoked"}, 201)


class TokenRefresherResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        return make_response({"access_token": new_token}, 201)
