from flask_jwt_extended import jwt_required
from flask_restful import Resource

from flaskr.db.dao.data import PrevisaoSolo


class StemporalResource(Resource):
    @jwt_required
    def post(self, ref_bacen):
        previsao_instance = PrevisaoSolo()
        stemporal = previsao_instance.get_all_stemporal(ref_bacen)

        format_stemporal = []
        for dado in stemporal:
            Ref_Bacen = int(dado[0])
            mae = (float(dado[1]),)
            rmse = (float(dado[2]),)
            r2 = (float(dado[3]),)
            Previsao = (float(dado[4]),)
            DataTeste = (str(dado[5]),)
            NDVIReal = float(dado[6])

            previsao_dict = {
                "ref_bacen": Ref_Bacen,
                "mae": mae,
                "rmse": rmse,
                "r2": r2,
                "previsao": Previsao,
                "data_teste": DataTeste,
                "NDVIReal": NDVIReal,
            }

            format_stemporal.append(previsao_dict)
        return format_stemporal
