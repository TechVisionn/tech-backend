from datetime import timedelta

from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flaskr.db.mongo_serve import conn_mongo_main

ACCESS_EXPIRES = timedelta(hours=12)
REFRESH_EXPIRES = timedelta(hours=24)

def config_jwt_token(app):
    # Security with Flast JWT Extended
    app.config["JWT_SECRET_KEY"] = ""
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = REFRESH_EXPIRES

    jwt = JWTManager(app)
    
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        db_instance = conn_mongo_main()
        jti = jwt_payload["jti"]
        revoked_token = db_instance.token.find_one({"jti": jti})
        return revoked_token is not None

    return jwt

def config_app_cors(app):
    # Config Cors
    CORS(app, resources={r"*": {"origins": "*"}})
