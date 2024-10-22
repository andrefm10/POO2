
class Despesa:
    def __init__(self, valor, categoria, data, descricao):
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao


    def __str__(self):
        return f"R$ {self.valor} - registrada no dia {self.data} - Descrição: {self.descricao};"
    
    def __repr__(self):
        return self.__str__()
    
    def get_valor(self):
        return self.valor
    
    def get_categoria(self):
        return self.categoria
    
    def get_data(self):
        return self.data