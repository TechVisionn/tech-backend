DRIVER = "{}"

# Local conection
SERVER = "" # DB server
DATABASE = ""
UID = ""
PASSWORD = ""


def get_connection_string():
    return "DRIVER={};SERVER={};DATABASE={};UID={};PWD={}".format(
        DRIVER,
        SERVER,
        DATABASE,
        UID,
        PASSWORD
    )
