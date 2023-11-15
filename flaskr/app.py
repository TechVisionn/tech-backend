import os

from flask import Flask

from flaskr.routes import config_app_routes
from flaskr.security import config_app_cors, config_jwt_token
from flaskr.services.user_validation import user_validation

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['DEBUG'] = int(os.environ.get('FLASK_DEBUG', '0')) == 1

# Config Flask JWT Extended
jwt = config_jwt_token(app)

# Config App CORS
config_app_cors(app)

# Validation users
user_validation.user_validation_limbo()

# Config Flask Restful
api = config_app_routes(app)

if __name__ == "__main__":
    app.run()
