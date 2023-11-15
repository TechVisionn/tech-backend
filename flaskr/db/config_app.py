import json


def config_mysql():
    with open("/home/zarruda/faculdade/api/tech-backend/flaskr/db/configs/config_mysql.json", 'r') as json_file:
        config_mysql = json.load(json_file)
    return config_mysql

instance_mysql = config_mysql()

DRIVER = instance_mysql["conn_mysql"]["driver"]
SERVER = instance_mysql["conn_mysql"]["server"]
DATABASE = instance_mysql["conn_mysql"]["database"]
UID = instance_mysql["conn_mysql"]["uid"]
PASSWORD = instance_mysql["conn_mysql"]["password"]

def get_connection_string():
    
    return "DRIVER={};SERVER={};DATABASE={};UID={};PWD={}".format(
        DRIVER,
        SERVER,
        DATABASE,
        UID,
        PASSWORD
    )