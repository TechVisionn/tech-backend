from datetime import datetime

from bson import ObjectId
from flask import make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from flaskr.db.mongo_serve import conn_mongo_main, conn_mongo_validation


class TermsResource(Resource):
    def __init__(self):
        super().__init__()

        db_instance_main = conn_mongo_main()
        db_instance_validation = conn_mongo_validation()

        self.user_instance = db_instance_main.user
        self.user_history = db_instance_main.history
        self.term_instance = db_instance_main.Term

        self.validation_instance = db_instance_validation.validation

    @jwt_required()
    def post(self):
        _term = request.json.get("_term")
        _term_option_one = request.json.get("_option_one")
        _term_option_second = request.json.get("_option_second")

        _current_user_id = get_jwt_identity()
        user_history = self.user_history.find_one(
            {"id_user": ObjectId(_current_user_id)}, sort=[("timestamp", -1)]
        )
        term = self.term_instance.find_one(user_history["id_term"])

        if _term is False:
            self.user_history.insert_one(
                {
                    "id_user": user_history["id_user"],
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
                    "id_user": ObjectId(_current_user_id),
                    "id_term": term["_id"],
                    "date_of_refusal": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            self.user_instance.delete_one({"_id": ObjectId(_current_user_id)})
            self.user_validation.delete_one({"id_user": ObjectId(_current_user_id)})
            return make_response({"message": "User is deleted"})

        if (
            _term_option_one == user_history["parameters"]["option_one"]
            and _term_option_second == user_history["parameters"]["option_second"]
        ):
            return make_response({"message": "terms equals"})

        else:
            self.user_history.insert_one(
                {
                    "id_user": user_history["id_user"],
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
            return make_response({"message": "terms update"})
