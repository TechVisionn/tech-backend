# import os

# import pandas as pd
# from fpdf import FPDF
# from sqlalchemy import text

# from flaskr.db import db_instance


# class GlebaService:
#     def generete_query_to_pdf(self, ref_bacen):
#         query = text("""
#                 SELECT
#                     GlebaInfo.Numero_RefBacen,
#                     GlebaInfo.Numero_Ordem,
#                     GlebaInfo.Cod_Identificador_Gleba,
#                     GlebaInfo.Numero_Gleba,
#                     GlebaInfo.Altitute,
#                     GlebaInfo.NU_INDICE_PONTO,
#                     GlebaInfo.Coordenas,
#                     S5.DT_EMISSAO AS DATA_EMISSAO_REFBACEN,
#                     CASE 
#                         WHEN S5.CD_ESTADO = 'SP' THEN 'São Paulo'
#                         ELSE S5.CD_ESTADO 
#                     END AS ESTADO,
#                     S5.CD_TIPO_SEGURO AS TIPO_SEGURO,
#                     S5.DT_FIM_PLANTIO AS DATA_PLANTIO,
#                     S5.CD_TIPO_IRRIGACAO AS TIPO_IRRIGACAO,
#                     S5.VL_ALIQ_PROAGRO AS VALOR_ALIQUOTA,
#                     S5.CD_TIPO_CULTIVO AS TIPO_CULTIVO,
#                     S5.CD_TIPO_GRAO_SEMENTE AS TIPO_GRAO,
#                     S5.VL_JUROS AS JUROS_INVESTIMENTO,
#                     S5.VL_RECEITA_BRUTA_ESPERADA AS RECEITA_BRUTA_ESTIMADA,
#                     S5.DT_FIM_COLHEITA AS DATA_FIM_COLHEITA,
#                     S5.VL_PERC_CUSTO_EFET_TOTAL AS CUSTO_TOTAL
#                 FROM
#                 (SELECT 
#                     MAX(REF_BACEN) AS Numero_RefBacen, 
#                     MAX(NU_ORDEM) AS Numero_Ordem, 
#                     MAX(NU_IDENTIFICADOR) AS Cod_Identificador_Gleba, 
#                     MAX(NU_INDICE_GLEBA) AS Numero_Gleba,
#                     MAX(CGL_VL_ALTITUDE) AS Altitute,
#                     MAX(NU_INDICE_PONTO) AS NU_INDICE_PONTO,
#                     CONCAT('MULTIPOINT(', GROUP_CONCAT(CONCAT(REPLACE(VL_LATITUDE, ',', '.'), ' ', REPLACE(VL_LONGITUDE, ',', '.')) SEPARATOR ', '), ')') AS Coordenas
#                 FROM glebas_sp
#                 WHERE REF_BACEN = :ref_bacen) AS GlebaInfo
#                 JOIN saida5 S5 ON S5.REF_BACEN = :ref_bacen limit 1;""")
        
#         result = db_instance.session.execute(query, {'ref_bacen': ref_bacen})
#         data_list = []

#         for row in result:
#             data = {
#                 'Numero_RefBacen': row[0],
#                 'Numero_Ordem': row[1],
#                 'Cod_Identificador_Gleba': row[2],
#                 'Numero_Gleba': row[3],
#                 'Altitute': row[4],
#                 'Dt emissão ref_bacen': row[7],
#                 'Estado': row[8],
#                 'Tipo Seguro': row[9],
#                 'Data Plantio': row[10],
#                 'Tipo Irrigação': row[11],
#                 'Valor Aliquota': row[12],
#                 'Tipo Cultivo': row[13],
#                 'Tipo Grão': row[14],
#                 'Juros Investimento': row[15],
#                 'Receita Bruta Estimada': row[16],
#                 'Data fim Colheita': row[17],
#                 'Custo Total': row[18],
#                 'Coordenas': row[6]
#             }
#             data_list.append(data)
        
#         pdf = FPDF()
#         pdf.set_font('Arial', 'B', 12)
#         pdf.add_page()
#         pdf.cell(0, 10, 'Relatório de Glebas', 0, 1, 'C')
#         pdf.set_font('Arial', 'B', 12)
#         pdf.cell(0, 10, 'Glebas', 0, 1, 'L')
#         pdf.ln(10)
        
#         for data in data_list:
#             pdf.set_font('Arial', 'B', 12)
#             pdf.cell(0, 10, 'Informações da Gleba', 0, 1, 'L')
#             pdf.set_font('Arial', '', 12)
#             for key, value in data.items():
#                 if key == 'Coordenas':
#                     pdf.set_font('Arial', 'B', 12)
#                     pdf.cell(0, 10, f'{key}:', 0)
#                     pdf.ln()
#                     pdf.set_font('Arial', '', 12)
#                     pdf.multi_cell(0, 10, value, 0, 'L')
#                 else:
#                     pdf.set_font('Arial', 'B', 12)
#                     pdf.cell(60, 10, f'{key}:', 0)
#                     pdf.set_font('Arial', '', 12)
#                     pdf.cell(0, 10, str(value), 0, 1)
#             pdf.ln(15)
#         download_path = os.path.expanduser("~/Downloads")
#         pdf_path = os.path.join(download_path, "Glebas.pdf")
#         pdf.output(pdf_path)
#         return "Glebas.pdf"
