from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.dao.gleba import GlebaDao


class GlebaResource(Resource):

    @jwt_required()
    def post(self):
        lowest_latitude = request.json.get("lowest_latitude")
        greatest_latitude = request.json.get("greatest_latitude")
        lowest_longitude = request.json.get("lowest_longitude")
        greatest_longitude = request.json.get("greatest_longitude")

        gleba_dao = GlebaDao()
        glebas = gleba_dao.query_return_land(
            lowest_latitude, greatest_latitude, lowest_longitude, greatest_longitude
        )

        format_glebas = []
        for dado in glebas:
            nu_identificador = int(dado[0])
            data_emissao = dado[2]
            data_plantio = dado[5]
            data_fim_colheita = dado[11]
            tp_seguro = dado[4]
            estado = dado[3]
            tipo_irrigacao = dado[6]
            tipo_grao = dado[7]
            valor_aliquota = dado[8]
            juros_investimentos = dado[9]
            receita_bruta = float(dado[10])
            coordenadas_str = dado[1]
            coordenadas = eval(coordenadas_str)

            gleba_dict = {
                "nu_identificador": nu_identificador,
                "data_emissao": data_emissao,
                "data_plantio": data_plantio,
                "data_fim_colheita": data_fim_colheita,
                "tp_seguro": tp_seguro,
                "estado": estado,
                "tipo_irrigacao": tipo_irrigacao,
                "tipo_grao": tipo_grao,
                "valor_aliquota": valor_aliquota,
                "juros_investimentos": juros_investimentos,
                "receita_bruta": receita_bruta,
                "coordenadas": coordenadas,
            }

            format_glebas.append(gleba_dict)
        return format_glebas
