from flask import request
from flask_restful import Resource
from flask import jsonify
from flaskr.models.sicor_gleba import SicorGlebaModel
 
class GlebaResource(Resource):
    def post(self):
        ref_bacen = request.json.get("ref_bacen")
        glebas = SicorGlebaModel.get_glebas_per_ref_bacen(ref_bacen)
        gleba_dicts = []
        for gleba in glebas:
            gleba_dict = {
                'ref_bacen_FK': gleba[0],
                'nu_ordem_FK': gleba[1],
                'vl_vertices': gleba[2],
            }
            gleba_dicts.append(gleba_dict)

        return jsonify({"glebas": gleba_dicts})