from geoalchemy2 import Geometry, functions
from sqlalchemy import ForeignKey

import flaskr.config_app as ca

from flaskr.db import db_instance
from flaskr.models.sicor_op_estado import SicorOpEstadoModel


class SicorGlebaModel(db_instance.Model):
    _tablename_ = "sicor_gleba"
    _table__args_ = {"schema": ca.VISIONA_DB_SCHEMA}

    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    nu_identificador = db_instance.Column(db_instance.Integer)
    vl_vertices = db_instance.Column(Geometry(geometry_type="POINT"))
    cgl_vl_altitude = db_instance.Column(db_instance.Float)
    nu_ordem_FK = db_instance.Column(
        db_instance.Integer, ForeignKey("sicor_operacao_por_estado.nu_ordem")
    )
    ref_bacen_FK = db_instance.Column(
        db_instance.Integer, ForeignKey("sicor_operacao_por_estado.ref_bacen")
    )
    @classmethod
    def get_glebas_per_ref_bacen(cls, ref_bacen):
        return (
            db_instance.session.query(
                cls.ref_bacen_FK,
                cls.nu_ordem_FK,
                functions.ST_AsText(cls.vl_vertices).label("vl_vertices")
            )
            .filter(cls.ref_bacen_FK == ref_bacen)
        )