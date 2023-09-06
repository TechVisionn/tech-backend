from flaskr.db import db_instance, db_persist
from geoalchemy2 import Geometry


class SicorOpEstado:
    __tablename__ = "sicor_operacao_por_estado"

    ref_bacen = db_instance.Column(db_instance.Integer, primary_key=True)
    nu_ordem = db_instance.Column(db_instance.Integer, primary_key=True)
    cd_estado = db_instance.Column(db_instance.String(3))
    dt_fim_colheita = db_instance.Column(db_instance.Date)
    dt_fim_plantio = db_instance.Column(db_instance.Date)
    dt_inic_colheita = db_instance.Column(db_instance.Date)
    dt_inic_plantio = db_instance.Column(db_instance.Date)
    cd_programa = db_instance.Column(db_instance.String(256))
    cd_subprograma = db_instance.Column(db_instance.String(256))
    vl_receita_bruta_esperada = db_instance.Column(db_instance.Float)
    vl_rec_proprio_srv = db_instance.Column(db_instance.Float)
    vl_aliq_proagro = db_instance.Column(db_instance.Float)
    vl_juros = db_instance.Column(db_instance.Float)
    vl_juros_enc_finan_posfix = db_instance.Column(db_instance.Float)
    vl_area_financ = db_instance.Column(db_instance.Float)
    nu_identificador = db_instance.Column(db_instance.Integer)
    vl_vertices = db_instance.Column(db_instance.Geometry(geometry_type="POLYGON"))
    cgl_vl_altitude = db_instance.Column(db_instance.Float)

    @db_persist
    def save(self):
        db_instance.session.merge(self)
