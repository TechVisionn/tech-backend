# ========================== Data Access Classes ==========================
# ATTENTION:
#   All classes that refers to a DB table shall:
#       1) Extend the class Entity define in entity.py
#       2) Have the exact name of the table in DB (is not case sensitive)
#       3) Have all the DB table columns in the __init__(...) method with default values.
#           (The parameters shall have exactly the same name of the columns)
#       4) Have the "id" field, with this exact name
# ========================== Data Access Classes ==========================


# The init_attrs function is a utility function that takes two arguments:
# obj (an object) and fldsDict (a dictionary). It copies the key-value pairs
# from the fldsDict dictionary to the obj object's attributes, allowing
# dynamic initialization of the object's attributes based on the values
# ​​provided in the dictionary. The "self" key is deleted from the fldsDict
# dictionary to avoid assigning the object itself as an attribute.


import redis

from flaskr.db.entity import Entity
from flaskr.db.redis_server import redis_available, redis_server

# # Utility function
# def init_attrs(obj, fldsDict):
#     localsCpy = dict(fldsDict)
#     del localsCpy["self"]
#     for k, v in localsCpy.items():
#         setattr(obj, k, v)


class GlebaDao(Entity):
    def __init__(self):  # Add Coluns of table here
        # The current class is a subclass of the Entity,
        # therefore the Entity must start first
        super().__init__()

    def query_return_land(
        self, lowest_latitude, greatest_latitude, lowest_longitude, greatest_longitude
    ):
        cache_key = f"gleba:{lowest_latitude}:{greatest_latitude}:{lowest_longitude}:{greatest_longitude}"

        try:
            if redis_available:
                cached_data = redis_server.get(cache_key)
                if cached_data:
                    result = cached_data
                    return eval(result)
        except redis.ConnectionError:
            print("Não foi possível conectar ao servidor Redis")

        """
        Catch everything with limit
        """
        sql = f"""
        SELECT 
           Glebas.REF_BACEN,
            CONCAT(GROUP_CONCAT(CONCAT('[', REPLACE(Glebas.LATITUDE, ',', '.'), ', ', REPLACE(Glebas.LONGITUDE, ',', '.'), ']') 
            ORDER BY CAST(Glebas.NU_INDICE_PONTO AS SIGNED) SEPARATOR ', ')) AS Coordenadas,
            S5.DT_EMISSAO AS DATA_EMISSAO_REFBACEN,
        CASE WHEN 
            S5.CD_ESTADO = 'SP' THEN 'São Paulo'
        ELSE 
            S5.CD_ESTADO 
        END AS ESTADO,
            GARAN_EMPREEND.DESCRICAO AS TIPO_SEGURO,
            S5.DT_FIM_PLANTIO AS DATA_PLANTIO,
            GRAO_IRRIG.DESCRICAO AS TIPO_IRRIGACAO,
            GRAO.DESCRICAO AS TIPO_GRAO,
            S5.VL_ALIQ_PROAGRO AS VALOR_ALIQUOTA,
            S5.VL_JUROS AS JUROS_INVESTIMENTO,
            S5.VL_RECEITA_BRUTA_ESPERADA AS RECEITA_BRUTA_ESTIMADA,
            S5.DT_FIM_COLHEITA AS DATA_FIM_COLHEITA
        FROM (
        SELECT 
            GLP.REF_BACEN,
            REPLACE(VL_LATITUDE, ',', '.') AS LATITUDE,
            REPLACE(VL_LONGITUDE, ',', '.') AS LONGITUDE,
            CAST(NU_INDICE_PONTO AS SIGNED) AS NU_INDICE_PONTO
        FROM 
            techdata.glebas_sp GLP
            JOIN techdata.saida5 S5 ON S5.REF_BACEN = GLP.REF_BACEN
        WHERE
            CAST(REPLACE(VL_LATITUDE, ',', '.') AS DECIMAL(10, 10)) BETWEEN 
            CAST( {lowest_latitude} AS DECIMAL(10, 10)) 
        AND 
            CAST( {greatest_latitude} AS DECIMAL(10, 10))
        AND 
            CAST(REPLACE(VL_LONGITUDE, ',', '.') AS DECIMAL(10, 10)) BETWEEN
            CAST( {lowest_longitude} AS DECIMAL(10, 10)) AND 
            CAST( {greatest_longitude} AS DECIMAL(10, 10))LIMIT 150000) AS Glebas
        JOIN 
            techdata.saida5 S5 ON S5.REF_BACEN = Glebas.REF_BACEN
        LEFT JOIN  
            techvision.grao_semente GRAO ON GRAO.CODIGO = S5.CD_TIPO_GRAO_SEMENTE
        LEFT JOIN  
            techvision.tipo_irrigacao GRAO_IRRIG ON GRAO_IRRIG.CODIGO = S5.CD_TIPO_IRRIGACAO
        LEFT JOIN (
		SELECT 
			CODIGO, 
			DESCRICAO
		FROM 
			techvision.tipo_garantia_empreendimento) 
            AS GARAN_EMPREEND ON GARAN_EMPREEND.CODIGO = S5.CD_TIPO_SEGURO
        GROUP BY
            Glebas.REF_BACEN, S5.DT_EMISSAO, 		
            S5.CD_ESTADO, GARAN_EMPREEND.DESCRICAO, 
            GRAO_IRRIG.DESCRICAO,
            GRAO.DESCRICAO,
            S5.DT_FIM_PLANTIO, S5.CD_TIPO_IRRIGACAO, 
            S5.VL_ALIQ_PROAGRO,	S5.CD_TIPO_CULTIVO, 
            S5.VL_JUROS, S5.VL_RECEITA_BRUTA_ESPERADA, 
            S5.DT_FIM_COLHEITA, S5.VL_PERC_CUSTO_EFET_TOTAL
        HAVING 
            CHAR_LENGTH(Coordenadas) <= 1000;
        """
        # print(f"Querying: {sql}")
        gleba_instance = GlebaDao()
        result = gleba_instance.exec_query(sql)
        try:
            if redis_available:
                redis_server.set(cache_key, str(result))
        except redis.ConnectionError:
            print("Não foi possível conectar ao servidor Redis")
        return result


class PrevisaoSolo(Entity):
    def __init__(self):
        super().__init__()

    def get_stemporal(self, ref_bacen):
        sql = f"""
        SELECT
            CONCAT('[', GROUP_CONCAT(DISTINCT DataTeste), ']') AS DataTeste,
            CONCAT('[', GROUP_CONCAT(DISTINCT NDVIReal), ']') AS NDVIReal,
            CONCAT('[', GROUP_CONCAT(DISTINCT Previsao), ']') AS Previsao
        FROM 
            techvision.previsao_solo
        WHERE 
            Ref_Bacen = {ref_bacen};
        """
        previsao_instance = PrevisaoSolo()
        result = previsao_instance.exec_query(sql)
        return result
