from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flaskr.db.dao.gleba import GlebaDao


class GlebaResource(Resource):

    @jwt_required
    def get(self):
        gleba_dao = GlebaDao()
        glebas = gleba_dao.get_all()
        print(glebas)
        return "glebas"