from flask import Flask
from flaskr.db import config_sql_alchemy, db_instance
from flaskr.migrate import load_migrate


app = Flask(__name__)

# Configurar SQLAlchemy
config_sql_alchemy(app)

# Load Flask Migrate
migrate = load_migrate(db_instance, app)

if __name__ == '__main__':
    app.run()
