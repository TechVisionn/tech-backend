from datetime import timedelta

from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flaskr.db.mongo_serve import db_instance


ACCESS_EXPIRES = timedelta(hours=12)
REFRESH_EXPIRES = timedelta(hours=24)

def config_jwt_token(app):
    # Security with Flast JWT Extended
    app.config["JWT_SECRET_KEY"] = "8f1948d1-34a2-4e40-a832-266280cc8031"
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = REFRESH_EXPIRES

    jwt = JWTManager(app)
    
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        revoked_token = db_instance.tokens_revogados.find_one({"jti": jti})
        return revoked_token is not None

    return jwt

def config_app_cors(app):
    # Config Cors
    CORS(app, resources={r"*": {"origins": "*"}})
