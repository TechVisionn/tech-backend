from requests import post

from flaskr.db.mongo_serve import conn_mongo_validation


class MessageService:
    def __init__(self):
        super().__init__()
        db_instance = conn_mongo_validation()
        self.user_instance = db_instance.users

    def send_email_everyone(self, enabled=False):
        if enabled:
            emails = MessageService.get_emails(self)

            data = {
                "from_addr": "zaion.arruda@fatec.sp.gov.br",
                "to_addrs": emails,
                "cc_addrs": ["zaion.arruda@fatec.sp.gov.br"],
                "subject": "Testando",
                "content": "Conteúdo do teste",
            }

            result = post("http://localhost:5001/send_email", json=data)
            print(emails)
            return result

    def get_emails(self):
        users = self.user_instance.find()
        emails = []
        for _user in users:
            emails.append(_user["email"])

        return emails

message_service = MessageService()