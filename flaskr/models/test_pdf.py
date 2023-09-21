import flaskr.config_app as ca
from flaskr.db import db_instance


class TestPdfModel(db_instance.Model):
    __tablename__ = "test_pdf"

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    nome_gleba = db_instance.Column(db_instance.String)
    numero_gleba = db_instance.Column(db_instance.Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()
