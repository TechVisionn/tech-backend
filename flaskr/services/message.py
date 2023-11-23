from flaskr.db.mongo_serve import conn_mongo_main


class MessageService:
    def __init__(self):
        super().__init__()
        db_instance = conn_mongo_main()
        self.user_instance = db_instance.user

    def send_email_everyone(self):
        emails = MessageService.get_emails()
        #call api
       
        return "api"
    
    def get_emails(self):
        users = self.user_instance.find()
        emails = []
        for _user in users:
            emails.append(_user["email"])

        return emails
