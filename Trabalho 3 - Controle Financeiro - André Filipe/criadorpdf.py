from fpdf import FPDF
from datetime import datetime

class CriadorPDF:
    def __init__(self,controle):
        self.controle = controle

    def gerar_pdf(self,nome_arquivo):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        pdf.cell(200, 10, txt="Relatório Financeiro - Despesas por Categoria", ln=True, align='C')
        pdf.ln(10)

        
        
        for categoria, dados_categoria in self.controle.categorias.items():
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=f"{categoria}:", ln=True, align='L')
            pdf.set_font("Arial", "", 12)

            cont_cat = 0
            if len(dados_categoria.despesas) == 0:
                pdf.cell(200, 10, txt="Nenhuma despesa registrada.", ln=True, align='L')
            else:
                for despesa in dados_categoria.despesas:
                    pdf.cell(200, 10, txt=f"{despesa}", ln=True, align='L')
                    cont_cat += despesa.get_valor()
            
                pdf.ln(5)
                pdf.set_font("Arial", "B", 12)
                pdf.cell(200, 10, txt=f"Valor total registrado na categoria: R$ {cont_cat:.2f}", ln=True, align='L')
                pdf.set_font("Arial", "", 12)
            
            
            pdf.ln(10)
        
        pdf.set_font("Arial", "B", 16)
        pdf.ln(10) 
        pdf.cell(200, 10, txt="Aumentos Significativos", ln=True, align='C')
        pdf.ln(5)
        pdf.set_font("Arial", "", 12)

        if self.controle.aumento:
            for cat, dados in self.controle.aumento.items():
                diff = dados['Aumento']
                data_anterior = dados['data_anterior']
                data_atual = dados['data_atual']
                pdf.cell(200, 10, txt=f"{cat}: Aumento de {diff:.2f}% do dia {data_anterior} pro dia {data_atual}.", ln=True, align='L')
        else:
            pdf.cell(200, 10, txt="Nenhum aumento significativo registrado.", ln=True, align='L')

        pdf.output(nome_arquivo)
        print(f"Relatório salvo como '{nome_arquivo}'")
        
def gerar_relatorio_pdf_por_data(self, data_especifica, nome_arquivo):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt=f"Relatório de Despesas - {data_especifica}", ln=True, align="C")
    
    
    mes = datetime.strptime(data_especifica, "%m/%Y").month
    ano = datetime.strptime(data_especifica, "%m/%Y").year

    
    for cat, categoria_obj in self.categorias.items():
        despesas_mes = [d for d in categoria_obj.despesas 
                        if datetime.strptime(d.data, "%d/%m/%Y").month == mes and 
                           datetime.strptime(d.data, "%d/%m/%Y").year == ano]

        if not despesas_mes:
            
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=f"Categoria: {cat} - Não há despesas cadastradas para {data_especifica}.", ln=True)
        else:
           
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=f"Categoria: {cat}", ln=True)
            pdf.set_font("Arial", "", 12)

            for d in despesas_mes:
                pdf.cell(200, 10, txt=str(d), ln=True)

            
            total_mes = sum([d.get_valor() for d in despesas_mes])
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=f"Total de despesas para {cat} em {data_especifica}: R$ {total_mes:.2f}", ln=True)
            pdf.ln(10)

    
    pdf.output(nome_arquivo)
    print(f"Relatório gerado: {nome_arquivo}")
