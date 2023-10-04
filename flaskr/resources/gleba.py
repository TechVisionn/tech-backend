from flask import request
from flask_restful import Resource

# from flaskr.services.gleba import GlebaService


class GlebaResource(Resource):
    def get(self):
        # ref_bacen = request.json.get("ref_bacen")
        # gleba_service = GlebaService()
        # glebas = gleba_service.generete_query_to_pdf(ref_bacen=ref_bacen)

        return "glebas"