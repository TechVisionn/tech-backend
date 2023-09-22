from geoalchemy2 import Geometry, functions

import flaskr.config_app as ca
from flaskr.db import db_instance

class GlebasSPModel(db_instance.Model):
    __tablename__ = 'glebassp'
    __table__args__ = {"schema": ca.VISIONA_DB_SCHEMA}
    
    ref_bacen = db_instance.Column(db_instance.String(100))
    nu_ordem = db_instance.Column(db_instance.String(100))
    nu_identificador = db_instance.Column(db_instance.String(100))
    nu_indice_gleba = db_instance.Column(db_instance.String(100))
    nu_indice_ponto = db_instance.Column(db_instance.String(100))
    vl_latitude = db_instance.Column(db_instance.String(100))
    vl_longitude = db_instance.Column(db_instance.String(100))
    vl_altitude = db_instance.Column(db_instance.String(100))
    cgl_vl_altitude = db_instance.Column(db_instance.String(100))
    vl_vertices = db_instance.Column(Geometry(geometry_type="POINT"))

