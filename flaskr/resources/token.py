from datetime import datetime

from bson import ObjectId
from flask import make_response, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Resource

from flaskr.db.mongo_serve import conn_mongo_main, conn_mongo_validation


class TokenResource(Resource):
    def __init__(self):
        super().__init__()

        db_instance_main = conn_mongo_main()
        db_instance_validation = conn_mongo_validation()

        self.token_instance = db_instance_main.token
        self.user_instance = db_instance_main.user
        self.user_history = db_instance_main.history
        self.term_instance = db_instance_main.Term

        self.validation_instance = db_instance_validation.validation

    def post(self):
        _user = request.json.get("_user")
        _email = request.json.get("_email")
        _pwd = request.json.get("_pwd")
        _term = request.json.get("_term")
        _term_option_one = request.json.get("_option_one")
        _term_option_second = request.json.get("_option_second")

        # set
        latest_term = self.term_instance.find_one(sort=[("version", -1)])
        user = self.user_instance.find_one(
            {"user": _user, "email": _email, "pwd": _pwd}
        )
        user_history = self.user_history.find_one(
            {"id_user": user["_id"]}, sort=[("timestamp", -1)]
        )

        if user is None:
            return make_response({"message": "Invalid username or password"})

        if user_history == None:
            if _term is False:
                self.user_instance.delete_one(
                    {"user": _user, "email": _email, "pwd": _pwd}
                )
                return make_response({"message": "User is deleted"})
            if _term is None:
                return make_response({"message": "User needs to update terms"})
            else:
                self.user_history.insert_one(
                    {
                        "id_user": user["_id"],
                        "id_term": latest_term["_id"],
                        "accepted_term": _term,
                        "update_date": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                        "parameters": {
                            "option_one": False
                            if _term_option_one is None
                            else _term_option_one,
                            "option_second": False
                            if _term_option_second is None
                            else _term_option_second,
                        },
                    }
                )
                return make_response({"message": "User update"})
        term = self.term_instance.find_one(user_history["id_term"])
        if latest_term["version"] != term["version"] or _term is False:
            if _term is None:
                return make_response({"message": "User needs to update terms"})
            if _term is False:
                self.user_history.insert_one(
                    {
                        "id_user": user["_id"],
                        "id_term": term["_id"],
                        "accepted_term": _term,
                        "update_date": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                        "parameters": {
                            "option_one": False
                            if _term_option_one is None
                            else _term_option_one,
                            "option_second": False
                            if _term_option_second is None
                            else _term_option_second,
                        },
                    }
                )
                self.validation_instance.insert_one(
                    {
                        "id_user": user["_id"],
                        "id_term": term["_id"],
                        "date_of_refusal": datetime.today().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                    }
                )
                self.user_instance.delete_one(
                    {"user": _user, "email": _email, "pwd": _pwd}
                )
                return make_response({"message": "User is deleted"})
            else:
                self.user_history.insert_one(
                    {
                        "id_user": user["_id"],
                        "id_term": term["_id"],
                        "accepted_term": _term,
                        "update_date": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                        "parameters": {
                            "option_one": _term_option_one,
                            "option_second": _term_option_second,
                        },
                    }
                )
                return make_response({"message": "User update"})

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
