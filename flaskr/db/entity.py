import flaskr.db.config_app as config
import pymysql


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
                "autocommit": True
            }
            self.cnxn = pymysql.connect(**connection_params)
            self.cursor = self.cnxn.cursor()

    # Function for run querys
    def exec_query(self, sql, as_dict=False):
            self.connect()
            obj_class = type(self)
            results = []

            for t in self.cursor.execute(sql):
                if as_dict:
                    cols = [column[0] for column in self.cursor.description]

                    # Turn tuples into dicts
                    tmp_dict = {}
                    for i in range(len(cols)):
                        tmp_dict[cols[i]] = t[i]

                    results.append(tmp_dict)
                else:
                    results.append(obj_class(*t))

            return results
# Ajustar
#   File "C:\Users\ZARRUDA\Desktop\Zaion\API - 6 Semestre\tech-backend\flaskr\db\entity.py", line 44, in exec_query
#     for t in self.cursor.execute(sql):
# TypeError: 'int' object is not iterable