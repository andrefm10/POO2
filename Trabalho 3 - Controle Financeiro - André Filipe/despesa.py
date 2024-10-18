
class Despesa:
    def __init__(self, valor, categoria, data, descricao):
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao


    def __str__(self):
        return f"Despesa de {self.categoria}, com valor de R$ {self.valor}, registrada no dia {self.data}. Descrição: {self.descricao}."