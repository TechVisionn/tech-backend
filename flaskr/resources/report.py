from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.dao.gleba import GlebaDao


class ReportResource(Resource):
    
    def get(self):
        gleba_dao = GlebaDao()
        report = gleba_dao.query_return_report()
        print(report)
        return report