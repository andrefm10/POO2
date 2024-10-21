from despesa import Despesa
from categoria import Categoria
from controle_financeiro import ControleFinanceiro


#lista_geral = []
lista_edu, lista_ene, lista_agua, lista_int, lista_ali, lista_trs, lista_res, lista_ent = ([] for _ in range(8))
cont_edu, cont_ene, cont_agua, cont_int, cont_ali, cont_trs, cont_res, cont_ent = (0 for _ in range(8))

controle = ControleFinanceiro({})

while True:

    op = int(input())

    match op:
        case 1:
            valor = int(input("Digite o valor da despesa: "))
            data = input("Digite a data do registro da despesa(dd/mm/aaaa): ")
            op1= int(input())

            match op1:
                case 1:
                    lista_edu = controle.nova_despesa(valor,data,"Educação",3000, lista_edu)
                    cont_edu = controle.check_limite("Educação",data,cont_edu)
                case 2:
                    lista_ene = controle.nova_despesa(valor,data,"Energia",1000, lista_ene)
                    cont_ene = controle.check_limite("Energia",data,cont_ene)
                case 3:
                    lista_agua = controle.nova_despesa(valor,data,"Água",700, lista_agua)
                    cont_agua = controle.check_limite("Água",data,cont_agua)
                case 4:
                    lista_int = controle.nova_despesa(valor,data,"Internet",500, lista_int)
                    cont_int = controle.check_limite("Internet",data,cont_int)
                case 5:
                    lista_trs = controle.nova_despesa(valor,data,"Transporte",2500, lista_trs)
                    cont_trs = controle.check_limite("Transporte",data,cont_trs)
                case 6:
                    lista_res = controle.nova_despesa(valor,data,"Residência",2000, lista_res)
                    cont_res = controle.check_limite("Residência",data,cont_res)
                case 7:
                    lista_ent = controle.nova_despesa(valor,data,"Entretenimento",1500, lista_ent)
                    cont_ent = controle.check_limite("Entretenimento",data,cont_ent)

                case _:
                    print("Opção inváida. Tente novamente depois.")
        
        case 2:
            print("Relatório categorizado: ")
            print("\nEducação:")
            controle.relatorio(lista_edu,cont_edu)
            print("\nEnergia:")
            controle.relatorio(lista_ene,cont_ene)
            print("\nÁgua:")
            controle.relatorio(lista_agua,cont_agua)
            print("\nInternet:")
            controle.relatorio(lista_int,cont_int)
            print("\nTransporte:")
            controle.relatorio(lista_trs,cont_trs)
            print("\nResidência:")
            controle.relatorio(lista_res,cont_res)
            print("\nEntretenimento:")
            controle.relatorio(lista_ent,cont_ent)

        case 3:
            aumentos = controle.check_aumento(lista_edu, 0.20)
            print(aumentos)
            
        
        case 5:
            break

        case _:
            print("Opção inváida. Tente novamente depois.")

                
                
            
                