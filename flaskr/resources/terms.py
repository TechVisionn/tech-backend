from flask_restful import Resource
from flaskr.db.mongo_serve import db_instance
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
)

from flask import make_response, request


class TermsResource(Resource):
    def __init__(self):
        super().__init__()
        self.token_instance = db_instance.token
        self.user_instance = db_instance.user
        self.user_history = db_instance.history
        self.term_instance = db_instance.Term

    def get(self):
        _term = request.json.get("_term")
        _term_option_one = request.json.get("_option_one")
        _term_option_second = request.json.get("_option_second")
        _current_user_id = get_jwt_identity()

        print(_current_user_id)
        return make_response({'retornou', 200})