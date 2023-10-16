import pymysql

import flaskr.db.config_app as config


class Entity:
    """This is a base DAO (Data Access Object) for all classes that represents a
    database table. Any class that extends Entity has the funcionality to save, update
    and delete your objects. Beside the persistence, the objects can execute SQL
    queries."""

    def __init__(self, cursor=None):
        # If create a new attribute that is not mapped in the DB table, its must
        # be deleted in the getAttributes() method.

        self.id = (
            -1
        )  # indicate that the connection object does not exist in the database

        if not cursor:
            self.cnxn = None
            self.cursor = None
        else:
            self.cursor = cursor

    # Connection Database
    def connect(self):
        if not self.cursor:
            connection_params = {
                "host": config.SERVER,
                "user": config.UID,
                "password": config.PASSWORD,
                "database": config.DATABASE,
                "autocommit": True,
            }
            self.cnxn = pymysql.connect(**connection_params)
            self.cursor = self.cnxn.cursor()

    # Function for run querys
    def exec_query(self, sql, as_dict=False):
        self.connect()
        self.cursor.execute(sql)
        if as_dict:
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = self.cursor.fetchall()
        return results
