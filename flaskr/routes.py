from flask_restful import Api

from flaskr.resources.gleba import GlebaResource


def config_app_routes(app):
    api = Api(app)

    __setting_route_doc(GlebaResource, "/gleba", api)

    return api


def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
