# ========================== Data Access Classes ========================== ===========================================================================
# ATTENTION:
#   All classes that refers to a DB table shall:
#       1) Extend the class Entity define in entity.py
#       2) Have the exact name of the table in DB (is not case sensitive)
#       3) Have all the DB table columns in the __init__(...) method with default values. (The parameters shall have exactly the same name of the columns)
#       4) Have the "id" field, with this exact name
# ========================== Data Access Classes ===========================================================================