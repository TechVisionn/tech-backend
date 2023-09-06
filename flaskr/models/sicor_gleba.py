from geoalchemy2 import Geometry
from sqlalchemy import ForeignKey

from flaskr.db import db_instance
from flaskr.models.sicor_op_estado import SicorOpEstado


class SicorGleba(db_instance.Model):
    __tablename__ = "sicor_gleba"

    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    nu_identificador = db_instance.Column(db_instance.Integer)
    vl_vertices = db_instance.Column(db_instance.Geometry(geometry_type="POLYGON"))
    cgl_vl_altitude = db_instance.Column(db_instance.Float)
    nu_ordem_FK = db_instance.Column(
        db_instance.Integer, ForeignKey("sicor_operacao_por_estado.nu_ordem")
    )
    ref_bacen_FK = db_instance.Column(
        db_instance.Integer, ForeignKey("sicor_operacao_por_estado.ref_bacen")
    )

    @classmethod
    def get_all(cls):
        return cls.query.all()
