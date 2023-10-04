from pymongo import MongoClient
from urllib.parse import quote_plus

MONGO_USER = ''
MONGO_PWD = ''
MONGO_HOST = ''
MONGO_DB = ''
# Codificando a senha para evitar conflitos com o caractere '@'
encoded_pwd = quote_plus(MONGO_PWD)

mongo_server = f'mongodb+srv://{MONGO_USER}:{encoded_pwd}@{MONGO_HOST}/{MONGO_DB}'
client = MongoClient(mongo_server)
db_instance = client[MONGO_DB]

