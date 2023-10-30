from datetime import datetime

from bson import ObjectId
from flask import make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from flaskr.db.mongo_serve import db_instance


class TermsResource(Resource):
    def __init__(self):
        super().__init__()
        self.user_instance = db_instance.user
        self.user_history = db_instance.history
        self.term_instance = db_instance.Term

    @jwt_required()
    def post(self):
        _term = request.json.get("_term")
        _term_option_one = request.json.get("_option_one")
        _term_option_second = request.json.get("_option_second")

        _current_user_id = get_jwt_identity()
        user = self.user_instance.find_one({"_id": ObjectId(_current_user_id)})

        if _term is False:
            self.user_instance.delete_one({"_id": ObjectId(_current_user_id)})
            self.user_history.update_many(
                        {"user": user['name']},
                        {"$unset": {"user": "", "pwd": ""}},
                    )
            return make_response({"message": "User is deleted"})
        
        if _term == None or _term_option_one == None or _term_option_second == None:
            return make_response({"message": "User needs to select terms"})

        if (
            _term_option_one == user["term"]["parameters"]["option_one"]
            and _term_option_second == user["term"]["parameters"]["option_second"]
        ):
            return make_response({"message": "terms equals"})

        else:
            _date_now = datetime.today().strftime("%Y-%m-%d")
            self.user_instance.update_one(
                {"_id": ObjectId(_current_user_id)},
                {
                    "$set": {
                        "date_accepted_term": _date_now,
                        "term": {
                            "parameters": {
                                "option_one": _term_option_one,
                                "option_second": _term_option_second,
                            }
                        }
                    }
                },
            )
            user_history_data = self.user_instance.find_one({"_id": ObjectId(_current_user_id)})
            self.user_history.insert_one(user_history_data)
