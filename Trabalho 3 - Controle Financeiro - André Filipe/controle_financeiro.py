from despesa import Despesa
from categoria import Categoria
from datetime import datetime

class ControleFinanceiro:
    def __init__(self, categorias):
        #categorias = {}
        self.categorias = categorias

    def __str__(self):
        return f"{self.categorias}"

    def nova_despesa(self,valor,data, cat, lim, lista):
        descricao = input("Descreva brevemente a despesa: ")
        d = Despesa(valor, cat, data, descricao)
        lista.append(d)
        c = Categoria(cat, lim, lista)
        self.categorias[cat] = c
        return lista
    
    def check_limite(self,cat,data, cont_total):
        mes = datetime.strptime(data, "%d/%m/%Y").month
        ano = datetime.strptime(data, "%d/%m/%Y").year
        
        aux = self.categorias[cat]

        despesas_mes = [d for d in aux.despesas 
                            if datetime.strptime(d.data, "%d/%m/%Y").month == mes and 
                               datetime.strptime(d.data, "%d/%m/%Y").year == ano]
        
        cont = sum([d.get_valor() for d in despesas_mes])
        cont_total += cont
        if cont > aux.limite:
            print(f"Alerta! O limite mensal de R$ {aux.limite} para essa categoria foi ultrapassado.")
        else:
            print("Gastos dentro do limite da categoria.")
        

        return cont_total
    
    def relatorio(self,lista,cont):
        if len(lista) == 0:
            print("Nâo há despesa cadastrada para essa categoria ainda.")
        else:
            for i in lista:
                print(i)
            print(f"Valor total registrado: R$ {cont}")
    
    def check_aumento(self,lista,teto):
        aumento = {}
        
        for i in lista:
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
                return "Não há despesas suficientes para análise"
            


             


            