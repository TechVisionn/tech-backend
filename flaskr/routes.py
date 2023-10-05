from flask_restful import Api

from flaskr.resources.gleba import GlebaResource
from flaskr.resources.user import UserResource

def config_app_routes(app):
    api = Api(app)

    __setting_route_doc(GlebaResource, "/gleba", api)
    __setting_route_doc(UserResource, "/users", api)

    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
