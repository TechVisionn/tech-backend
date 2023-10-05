from pymongo import MongoClient
from urllib.parse import quote_plus

MONGO_USER = ''
MONGO_PWD = ''
MONGO_HOST = ''
MONGO_DB = ''
# Codificando a senha para evitar conflitos com o caractere '@'
ENCONDE_PWD = quote_plus(MONGO_PWD)

mongo_server = f'mongodb+srv://{MONGO_USER}:{ENCONDE_PWD}@{MONGO_HOST}/{MONGO_DB}'
#Write_Concern = w=0
client = MongoClient(mongo_server, w=0)
db_instance = client[MONGO_DB]