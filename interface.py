import Funcionario as f
import funcoes as o
import os

def interfaceADM():
    while True:
        os.system('cls') 
        print("=========================================== OPÇÕES DE ADIMINISTRADOR ===========================================")
        print("OPÇÃO 1: EXIBIR INFORMAÇÕES DE FUNCIONÁRIOS\nOPÇÃO 2: EXIBIR INFORMAÇÕES DE CLIENTES\nOPÇÃO 3: CADASTRAR NOVO FUNCIONÁRIO\nOPÇÃO 4: CADASTRAR MUITOS FUNCIONÁRIOS\nOPÇÃO 5: CRIAR BASE DE DADOS DAS VAGAS")
        print("============================================= OPÇÕES OPERACIONAIS ==============================================")
        print("OPÇÃO 6: EXIBIR VAGAS OCUPAGAS\nOPÇÃO 7: CADASTRAR NOVO CLIENTE\nOPÇÃO 8: OCUPAR UMA VAGA\nOPÇÃO 9: DESOCUPAR VAGA\nOPÇÃO 10: SAIR DO MENU DE ADMINISTRADOR\n")
        try:
            opcao = int(input("Digite a opção "))
            if opcao == 1:
                os.system('cls')
                print("DESEJA EXIBIR:\nOPÇÃO 1: TODOS OS FUNCIONÁRIOS\nOPÇÃO 2: BUSCAR UM FUNCIONÁRIO POR ID")
                try:
                    exibir = int(input("DIGITE A OPÇÃO "))
                    if exibir == 1:
                        os.system('cls')
                        o.ordenar_funcionario()
                        o.exibir_funcionarios()
                    elif exibir == 2:
                        os.system('cls')
                        o.ordenar_funcionario()
                        try:
                            id = int(input("DIGITE O ID DO FUNCIONÁRIO "))
                            o.buscar_funcionario_por_id(id)
                        except ValueError as e:
                            print("APÉNAS NÚMEROS")
                        os.system('pause')
                except ValueError as g:
                    print("APÉNAS NÚMEROS")
            elif opcao == 2:
                os.system('cls')
                try:
                    print("DESEJA EXIBIR:\nOPÇÃO 1: TODOS OS CLIENTES\nOPÇÃO 2: BUSCAR UM CLIENTES POR CPF")
                    exibir = int(input("DIGITE A OPÇÃO "))
                    if exibir == 1:
                        os.system('cls')
                        try:
                            o.exibir_clientes()
                        except FileNotFoundError  as e:
                            print("NÃO HÁ CLIENTES AINDA")
                    elif exibir == 2:
                        os.system('cls')
                        try:
                            cpf = int(input("DIGITE O CPF DO CLIENTE (APÉNAS  NÚMEROS) "))
                            o.buscar_cliente_por_cpf(cpf)
                        except FileNotFoundError  as e:
                            print("NÃO HÁ CLIENTES AINDA") 
                        except ValueError as f:
                            print("APÉNAS NÚMEROS")
                except ValueError as g:
                    print("APÉNAS NÚMEROS")
                os.system('pause')
            elif opcao == 3:
                os.system('cls')
                print("O FUNCIONÁRIO É UM ADMINISTRADOR OU OPERADOR ?\nOPÇÃO 1: ADMINISTRADOR\nOPÇÃO 2: OPERADOR")
                try:
                    funcionario = int(input("DIGITE A OPÇÃO "))
                    if funcionario == 1:
                        os.system('cls')
                        o.cadastrar_adm()
                    elif funcionario == 2:
                        os.system('cls')
                        o.cadastrar_operador()
                except ValueError as e:
                    print("APÉNAS NÚMEROS")
            elif opcao == 4:
                os.system('cls')
                o.cadastrar_muitos_funcionarios()
            elif opcao == 5:
                os.system('cls')
                o.criar_base_dados_vagas()
            elif opcao == 6:
                os.system('cls')
                o.exibir_vagas_ocupadas()
            elif opcao == 7:
                os.system('cls')
                o.cadastrar_cliente()
            elif opcao == 8: 
                os.system('cls')
                o.buscar_vaga_livre()
            elif opcao == 9:
                os.system('cls')
                o.desocupar_vaga()
            elif opcao == 10: 
                break
            else:
                print("DIGITE UMA OPÇÃO VÁLIDA")
        except ValueError as h:
            print("APÉNAS NÚMEROS")
        

def interfaceOERACIONAL():
    while True:
        print("============================================= OPÇÕES OPERACIONAIS ==============================================")
        print("OPÇÃO 1: EXIBIR VAGAS OCUPAGAS\nOPÇÃO 2: OCUPAR UMA VAGA\nOPÇÃO 3: CADASTRAR NOVO CLIENTE\nOPÇÃO 4: DESOCUPAR VAGA\nOPÇÃO 5: SAIR DO MENU DE ADMINISTRADOR\n")
        try:
            opcao = int(input("Digite a opção "))
            if opcao == 1:
                os.system('cls')
                o.exibir_vagas_ocupadas()
            elif opcao == 2:
                os.system('cls')
                o.buscar_vaga_livre()
            elif opcao == 3:
                os.system('cls')
                o.cadastrar_cliente()
            elif opcao == 4:
                os.system('cls')
                o.desocupar_vaga()
            elif opcao == 5:
                break
            else:
                print("DIGITE UMA OPÇÃO VÁLIDA")
        except ValueError as h:
            print("APÉNAS NÚMEROS")