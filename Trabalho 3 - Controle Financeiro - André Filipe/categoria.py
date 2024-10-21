class Categoria:
    def __init__(self,nome, limite, despesas):
        self.nome = nome
        self.limite = limite
        self.despesas = despesas
        

    def __str__(self):
        despesas_str = "\n".join([str(despesa) for despesa in self.despesas])
        return f"{despesas_str}"
    
    def __repr__(self):
        return self.__str__()
   