from controle_financeiro import ControleFinanceiro
from criadorpdf import CriadorPDF

lista_edu, lista_ene, lista_agua, lista_int, lista_ali, lista_trs, lista_res, lista_ent = ([] for _ in range(8))
cont_edu, cont_ene, cont_agua, cont_int, cont_ali, cont_trs, cont_res, cont_ent = (0 for _ in range(8))

controle = ControleFinanceiro({})

while True:
    print("\nBem vindo ao sistema de controle financeiro, escolha uma opção:")
    print("1-Registrar despesa")
    print("2-Relatório por categorias")
    print("3-Checar aumentos significativos")
    print("4-Gerar relatório em PDF")
    print("5-Relatório mensal")
    print("6-Encerrar programa")
    op = int(input())

    match op:
        case 1:
            print("Siga corretamente os passos a seguir para registrar uma despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            data = input("Digite a data do registro da despesa(dd/mm/aaaa): ")
            print("Agora escolha uma das categorias apresentadas abaixo: \n1-Educação\n2-Energia\n3-Água\n4-Internet\n5-Alimentação\n6-Transporte\n7-Residência\n8-Entretenimento")
            op1= int(input())

            match op1:
                case 1:
                    lista_edu = controle.nova_despesa(valor,data,"Educação",3000, lista_edu)
                    cont_edu = controle.check_limite("Educação",data)
                    controle.check_aumento(cont_edu,30,"Educação",valor)
                case 2:
                    lista_ene = controle.nova_despesa(valor,data,"Energia",1000, lista_ene)
                    cont_ene = controle.check_limite("Energia",data)
                    controle.check_aumento(cont_ene,15,"Energia",valor)
                case 3:
                    lista_agua = controle.nova_despesa(valor,data,"Água",700, lista_agua)
                    cont_agua = controle.check_limite("Água",data)
                    controle.check_aumento(cont_agua,10,"Água",valor)
                case 4:
                    lista_int = controle.nova_despesa(valor,data,"Internet",500, lista_int)
                    cont_int = controle.check_limite("Internet",data)
                    controle.check_aumento(cont_int,15,"Internet",valor)
                case 5:
                    lista_ali = controle.nova_despesa(valor,data,"Alimentação",2500, lista_ali)
                    cont_ali = controle.check_limite("Alimentação",data)
                    controle.check_aumento(cont_ali,25,"Alimentação",valor)
                case 6:
                    lista_trs = controle.nova_despesa(valor,data,"Transporte",2500, lista_trs)
                    cont_trs = controle.check_limite("Transporte",data)
                    controle.check_aumento(cont_trs,30,"Transporte",valor)                   
                case 7:
                    lista_res = controle.nova_despesa(valor,data,"Residência",2000, lista_res)
                    cont_res = controle.check_limite("Residência",data)
                    controle.check_aumento(cont_res,10,"Residência",valor)
                case 8:
                    lista_ent = controle.nova_despesa(valor,data,"Entretenimento",1500, lista_ent)
                    cont_ent = controle.check_limite("Entretenimento",data)
                    controle.check_aumento(cont_ent,40,"Entretenimento",valor)
                
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
            print("\nAlimentação:")
            controle.relatorio(lista_ali,cont_ali)
            print("\nTransporte:")
            controle.relatorio(lista_trs,cont_trs)
            print("\nResidência:")
            controle.relatorio(lista_res,cont_res)
            print("\nEntretenimento:")
            controle.relatorio(lista_ent,cont_ent)

        case 3:
            controle.relatorio_aumento()
            
        case 4:
            res = input("Realmente deseja criar o relatório em PDF? Ele será baixado no seu sistema. (S ou N)").upper()
            if res == "S":
                pdf = CriadorPDF(controle)
                pdf.gerar_pdf(input("Digite o nome desejado pro arquivo(final .pdf): "))
            else:
                print("Entendido. Voltando para o menu.")
                continue
        
        case 5:
            datae = input("Digite um mês de um ano para analisar seu relatório(formato mm/aaaa): ")
            print()
            controle.gerar_relatorio_terminal_por_data("Educação",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Energia",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Água",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Internet",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Alimentação",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Transporte",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Residência",datae)
            print()
            controle.gerar_relatorio_terminal_por_data("Entretenimento",datae)

            
        
        case 6:
            print("O programa será encerrado.")
            break

        case _:
            print("Opção inváida. Tente novamente depois.")

                
                
            
                