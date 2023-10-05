from flask_restful import Resource

from flaskr.db.dao.gleba import GlebaDao


class GlebaResource(Resource):
    def get(self):
        gleba_dao = GlebaDao()
        glebas = gleba_dao.get_all()
        print(glebas)
        return "glebas"