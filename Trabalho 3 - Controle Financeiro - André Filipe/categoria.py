class Categoria:
    def __init__(self,nome, despesas):
        self.nome = nome
        self.despesas = despesas
        self.lista_geral = []
    
    def adicionar_lista(self,d):
        self.lista_geral.append(d)
    
    def printar(self):
        for i in self.lista_geral:
            print(i)