from flask_restful import Api

from flaskr.resources.gleba import GlebaResource
from flaskr.resources.report import ReportResource
from flaskr.resources.terms import TermsResource
from flaskr.resources.token import TokenRefresherResource, TokenResource
from flaskr.resources.user import UserResource


def config_app_routes(app):
    api = Api(app)

    __setting_route_doc(GlebaResource, "/gleba", api)
    __setting_route_doc(UserResource, "/user", api)
    __setting_route_doc(ReportResource, "/report", api)
    __setting_route_doc(TermsResource, "/terms", api)
    __setting_route_doc(TokenResource, "/token", api)
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api)

    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
