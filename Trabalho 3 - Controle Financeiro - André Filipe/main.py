from despesa import Despesa
from categoria import Categoria

#lista_geral = []
lista_edu = []

op = int(input())

match op:
    case 1:
        valor = int(input("Digite o valor da despesa: "))
        data = input("Digite a data do registro da despesa(dd/mm/aaaa): ")
        op1= int(input())

        match op1:
            case 1:
                descricao = input("Descreva brevemente essa desoesa: ")
                d = Despesa(valor,"Educação", data, descricao)
                lista_edu.append(d)
                c = Categoria("Educação", lista_edu)
                
                
                #lista_geral.append(d)
                #lista_edu.append(d)
                