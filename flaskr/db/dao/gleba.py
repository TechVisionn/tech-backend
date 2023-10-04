from flaskr.db.entity import Entity

# The init_attrs function is a utility function that takes two arguments:
# obj (an object) and fldsDict (a dictionary). It copies the key-value pairs
# from the fldsDict dictionary to the obj object's attributes, allowing
# dynamic initialization of the object's attributes based on the values
# ​​provided in the dictionary. The "self" key is deleted from the fldsDict
# dictionary to avoid assigning the object itself as an attribute.


# # Utility function
# def init_attrs(obj, fldsDict):
#     localsCpy = dict(fldsDict)
#     del localsCpy["self"]
#     for k, v in localsCpy.items():
#         setattr(obj, k, v)


class Gleba(Entity):
    def __init__(self,
            codigo = 0,
            descricao = ""):  # Add Coluns of table here#
        # The current class is a subclass of the Entity,
        # therefore the Entity must start first
        super().__init__()

        self.codigo = codigo
        self.descricao = descricao

    def get_all(self):  # Limit data return
        """
        Catch everything with limit
        """
        sql = f"SELECT * FROM atividade"
        print(f"Querying: {sql}")  # Imprimir o SQL para depuração
        gleba_instance = Gleba()
        result = gleba_instance.exec_query(sql)
        return result