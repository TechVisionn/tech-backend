from bson import ObjectId

from flaskr.db.mongo_serve import conn_mongo_main, conn_mongo_validation


class UserValidationService:
    def __init__(self):
        super().__init__()

        db_instance_main = conn_mongo_main()
        db_instance_validation = conn_mongo_validation()

        self.user_instance = db_instance_main.user
        self.validation_instance = db_instance_validation.validation

    def user_validation_limbo(self):
        users = self.user_instance.find()
        validation = self.validation_instance.find()

        users_ids_list = [str(user_ids["_id"]) for user_ids in users]
        validation_ids_list = [
            str(ids_validation["id_user"]) for ids_validation in validation
        ]

        for users_id in users_ids_list:
            if users_id in validation_ids_list:
                self.user_instance.delete_one({"_id": ObjectId(users_id)})
                print("Usuários deletados")
        print("Nenhum usuário deletado")


user_validation = UserValidationService()
