from flask import Flask
from flaskr.db import config_sql_alchemy, db_instance


app = Flask(__name__)

# Configurar SQLAlchemy
config_sql_alchemy(app)

if __name__ == '__main__':
    app.run()
