from datetime import datetime

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.dao.data import PrevisaoSolo


class StemporalResource(Resource):
    @jwt_required
    def post(self):
        ref_bacen = request.json.get("ref_bacen")
        previsao_instance = PrevisaoSolo()
        stemporal = previsao_instance.get_stemporal(ref_bacen)

        print(stemporal)
        format_stemporal = []
        for dado in stemporal:
            datas = [datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d") for date in dado[0][1:-1].split(',')]  # Convertendo para strings
            NDVIReal = [float(value) for value in dado[1][1:-1].split(',')]  # Convertendo para floats
            Previsao = [float(value) for value in dado[2][1:-1].split(',')]  # Convertendo para floats

            previsao_dict = {
                "data_teste": datas,
                "NDVIReal": NDVIReal,
                "previsao": Previsao,
            }

            format_stemporal.append(previsao_dict)
        return format_stemporal
