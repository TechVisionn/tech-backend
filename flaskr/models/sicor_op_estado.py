from sqlalchemy import PrimaryKeyConstraint

from flaskr.db import db_instance


class SicorOpEstadoModel(db_instance.Model):
    __tablename__ = "sicor_operacao_por_estado"
    __table_args__ = (PrimaryKeyConstraint("ref_bacen", "nu_ordem"),)

    ref_bacen = db_instance.Column(db_instance.Integer, index=True, nullable=False)
    nu_ordem = db_instance.Column(db_instance.Integer, index=True, nullable=False)

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

    @classmethod
    def get_all(cls):
        return cls.query.all()
