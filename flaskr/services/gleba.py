import pandas as pd
from fpdf import FPDF

from flaskr.models.test_pdf import TestPdfModel


class GlebaService:
    def __init__(self) -> None:
        self.test_pdf = TestPdfModel()

    def generete_query_to_pdf(self):
        query = self.test_pdf.get_all()
        results = [(i.nome_gleba, i.numero_gleba) for i in query]

        df = pd.DataFrame(results)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        col_widths = [pdf.w / 3.5, pdf.w / 3.5]

        headers = ["Nome da Gleba", "Número da Gleba"]

        for header in headers:
            pdf.cell(col_widths[0], 10, header, border=1)

        pdf.ln()

        for row in df.itertuples(index=False):
            for item in row:
                pdf.cell(col_widths[0], 10, str(item), border=1)
            pdf.ln()
        # alterar para baixar direto para donwloads
        pdf.output("Glebas.pdf")

        return "Glebas.pdf"
