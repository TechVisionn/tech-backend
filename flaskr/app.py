import os
from flask import Flask

from flaskr.db import config_sql_alchemy
from flaskr.routes import config_app_routes

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['DEBUG'] = int(os.environ.get('FLASK_DEBUG', '0')) == 1

# Configurar SQLAlchemy
config_sql_alchemy(app)

# Config Flask Restful
api = config_app_routes(app)

if __name__ == "__main__":
    app.run()
