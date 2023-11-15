from urllib.parse import quote_plus

from pymongo import MongoClient
import json


def config_mongo():
    with open("/home/zarruda/faculdade/api/tech-backend/flaskr/db/configs/config_mongo.json", 'r') as json_file:
        config_mongo = json.load(json_file)
    return config_mongo

def conn_mongo_main():

    instance_mongo_main = config_mongo()
    
    mongo_user_main = instance_mongo_main['conn_mongo_main']['mongo_user_main']
    mongo_pwd_main = instance_mongo_main['conn_mongo_main']['mongo_pwd_main']
    mongo_host_main = instance_mongo_main['conn_mongo_main']['mongo_host_main']
    mongo_db_main = instance_mongo_main['conn_mongo_main']['mongo_db_main']

    # Codificando a senha para evitar conflitos com o caractere '@'
    encode_pwd_main = quote_plus(mongo_pwd_main)

    mongo_server = f'mongodb+srv://{mongo_user_main}:{encode_pwd_main}@{mongo_host_main}/{mongo_db_main}'
    client = MongoClient(mongo_server, w=0)
    db_instance_main = client[mongo_db_main]
    return db_instance_main

def conn_mongo_validation():

    instance_mongo_validation = config_mongo()

    mongo_user_validation = instance_mongo_validation['conn_mongo_main']['mongo_user_validation']
    mongo_pwd_validation = instance_mongo_validation['conn_mongo_main']['mongo_pwd_validation']
    mongo_host_validation = instance_mongo_validation['conn_mongo_main']['mongo_host_validation']
    mongo_db_validation = instance_mongo_validation['conn_mongo_main']['mongo_db_validation']
    # Codificando a senha para evitar conflitos com o caractere '@'
    encode_pwd_validation = quote_plus(mongo_pwd_validation)

    mongo_server = f'mongodb+srv://{mongo_user_validation}:{encode_pwd_validation}@{mongo_host_validation}/{mongo_db_validation}'
    client = MongoClient(mongo_server, w=0)
    db_instance_validation = client[mongo_db_validation]
    return db_instance_validation