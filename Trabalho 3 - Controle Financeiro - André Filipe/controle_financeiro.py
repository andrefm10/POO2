from despesa import Despesa
from categoria import Categoria
from datetime import datetime

class ControleFinanceiro:
    def __init__(self, categorias):
        #categorias = {}
        self.categorias = categorias
        self.aumento = {}

    def __str__(self):
        return f"{self.categorias}"

    def nova_despesa(self,valor,data, cat, lim, lista):
        descricao = input("Descreva brevemente a despesa: ")
        d = Despesa(valor, cat, data, descricao)
        lista.append(d)
        c = Categoria(cat, lim, lista)
        self.categorias[cat] = c
        return lista
    
    def check_limite(self,cat,data):
        mes = datetime.strptime(data, "%d/%m/%Y").month
        ano = datetime.strptime(data, "%d/%m/%Y").year
        
        aux = self.categorias[cat]

        despesas_mes = [d for d in aux.despesas 
                            if datetime.strptime(d.data, "%d/%m/%Y").month == mes and 
                               datetime.strptime(d.data, "%d/%m/%Y").year == ano]
        
        cont = sum([d.get_valor() for d in despesas_mes])
        cont_total = sum([d.get_valor() for d in aux.despesas])

        if cont > aux.limite:
            print(f"Alerta! O limite mensal de R$ {aux.limite} para essa categoria foi ultrapassado. Despesa registrada.")
        else:
            print("Gastos dentro do limite da categoria. Despesa registrada.")
        

        return cont_total
    
    def relatorio(self,lista,cont):
        if len(lista) == 0:
            print("Nâo há despesa cadastrada para essa categoria ainda.")
        else:
            for i in lista:
                print(i)
            print(f"Valor total registrado: R$ {cont}")
    
    def check_aumento(self,cont,teto, cat, valor):
        aux = self.categorias[cat]

        if len(aux.despesas) < 2:
            return
        valor_atual = aux.despesas[-1].get_valor()
        valor_anterior = aux.despesas[-2].get_valor()

        dif = ((valor_atual - valor_anterior) / valor_anterior) * 100

        if dif > teto:
            self.aumento[cat] = {"Aumento": dif, "data_anterior": aux.despesas[-2].get_data(), "data_atual": aux.despesas[-1].get_data()}


    def relatorio_aumento(self):
        if self.aumento:
            print("Categorias com aumentos significativos:")
            for cat, i in self.aumento.items():
                diff = i["Aumento"]
                data_anterior = i["data_anterior"]
                data_atual = i["data_atual"]
                
                print(f"{cat}: Aumento de {diff:.2f}% do dia {data_anterior} pro dia {data_atual};")
        else:
            print("Nenhuma categoria teve aumento significativo.")

    def gerar_relatorio_terminal_por_data(self, cat, data_especifica):
        if cat not in self.categorias:
            print(f"Ainda não há despesas registradas em {cat}")
            return
        mes = datetime.strptime(data_especifica, "%m/%Y").month
        ano = datetime.strptime(data_especifica, "%m/%Y").year

        aux = self.categorias[cat]

        despesas_mes = [d for d in aux.despesas 
                            if datetime.strptime(d.data, "%d/%m/%Y").month == mes and 
                            datetime.strptime(d.data, "%d/%m/%Y").year == ano]

        if not despesas_mes:
            print(f"Não há despesas cadastradas para {cat} em {data_especifica}.")
        else:
            
            print(f"{cat}:")
            

            for d in despesas_mes:
                print(d)

            total_mes = sum([d.get_valor() for d in despesas_mes])
            print(f"Valor total registrado no mês {data_especifica}: R$ {total_mes:.2f}")
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        '''for i in lista:
            if len(lista) >= 2:    
                ultima = lista[-1].get_valor()
                penultima = lista[-2].get_valor()

                dif = (ultima-penultima)/penultima 
                if dif > teto:
                    dif = dif*100
                    aumento[i.get_categoria()] = dif
                    return aumento
                else:
                    return "Não há aumentos significativos"
            else:
                return "Não há despesas suficientes para análise"'''
            


             


            