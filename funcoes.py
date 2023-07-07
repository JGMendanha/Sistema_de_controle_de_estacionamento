import random
import os
import Funcionario as f
import Vagas as v
import interface as i
import Cliente as c

# FUNÇÕES DE GERAR ID:
def gerar_id_adm():
    while True:
        id = random.randint(1000000, 9999999)
        if id % 2 == 0:
            return id

def gerar_id_operacional():
    while True:
        id = random.randint(1000000, 9999999)
        if id % 2 != 0:
            return id
        
def gerar_id():
    return random.randint(1000000, 9999999)
        

#FUNÇÕES DE CADASTRO:
def cadastrar_adm():
    try:
        nome = str(input("Diga o nome do administrador "))
        salario = float(input("Diga o salário do administrador "))
        cargo = str(input("Diga o cargo do adiministrador "))
    except ValueError as e:
        os.system('cls')
        cadastrar_adm()
    print("Será gerado um ID de 7 dígitos para seu administrador. Por favor, salve este ID, ele será usado como senha de acesso.")
    idAdm = gerar_id_adm()
    print("ID ->", idAdm)
    f1 = f.Funcionario(nome, idAdm, salario, cargo)
    salvar_funcionario(f1, f.arquivo)

def cadastrar_operador():
    try:
        nome = str(input("Diga o nome do operador "))
        salario = float(input("Diga o salário do operador "))
        cargo = str(input("Diga o cargo do operador "))
    except ValueError as e:
        os.system('cls')
        cadastrar_operador()
    print("Será gerado um ID de 7 dígitos para seu operador. Por favor, salve este ID, ele será usado como senha de acesso.")
    idOperador = gerar_id_operacional()
    print("ID ->", idOperador)
    f1 = f.Funcionario(nome, idOperador, salario, cargo)
    salvar_funcionario(f1, f.arquivo)

def cadastrar_muitos_funcionarios():
    quantidade = int(input("DIGA QUANTOS FUNCIONÁRIOS ALEATÓRIOS DESEJA CRIAR "))
    for i in range(quantidade):
        id = gerar_id()
        f1 = f.Funcionario("xxxx", id, 0, "xxxx")
        salvar_funcionario(f1, f.arquivo)
    print("========================================= SUCESSO AO CRIAR A BASE DE DADOS =========================================")
    os.system('pause')
    
def cadastrar_cliente():
    try:
        nome = str(input("Diga o nome do cliente "))
        cpf = int(input("Diga o cpf do cliente (APENAS NÚMEROS) "))
        placa_carro = str(input("Diga a placa do carro do cliente "))
    except  ValueError as e:
        cadastrar_cliente()
    c1 = c.Cliente(nome, cpf, placa_carro)
    salvar_cliente(c1, c.arquivo)


#FUNÇÕES DE SALVAR EM ARQUIVO:
def salvar_funcionario(funcionario, arquivo):
    with open(arquivo, 'a') as file: file.write(f"{funcionario.nome};{funcionario.salario};{funcionario.id};{funcionario.cargo}\n")
    file.close()

def salvar_cliente(cliente, arquivo):
    with open(arquivo, 'a') as file: file.write(f"{cliente.nome};{cliente.cpf};{cliente.placa_carro}\n")
    file.close()


#FUNÇÃO DE DIRECIONAMENTO DE INTERFACE DE ACORDO COM O ID DO FUNCIONÁRIO:
def direcionamento_de_interface():
    while True:
        os.system('cls')
        print("===================================== BEM VINDO =====================================")
        print("DIGITE SEU ID PARA TER ACESSO A SUA INTERFACE DE TRABALHO")
        id = int(input("DIGITE SEU ID "))
        verifica_id = buscar_funcionario_sequencial_verifica(id)
        if id % 2 == 0 and verifica_id == True:
            print("Encontramos você, tenha um bom trabalho")
            os.system("pause")
            i.interfaceADM()
        elif id % 2 != 0 and verifica_id == True:
            print("Encontramos você, tenha um bom trabalho")
            os.system("pause")
            i.interfaceOERACIONAL()
        else:
            print("Infelizmente seu ID não consta na nossa base de dados. Verifique se digitou corretamente seu ID")
            os.system('pause')


#FUNÇÃO DE CRIAÇÃO DA BASE DE DADOS DAS VAGAS:
def criar_base_dados_vagas():
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    setores = int(input("Diga a quantidade de setores "))
    for i in range(setores):
        quantidade = int(input(f"Diga a quantidade de vagas no setor {letras[i]} "))
        for j in range(quantidade):
            nomeclatura = str(letras[i]) + str(j)
            v1 = v.Vagas(nomeclatura, "Livre")
            with open(v.arquivo, 'a') as file: file.write(f"{v1.nomeclatura};{v1.placa_carro_ocupante}\n")
    print("========================================= SUCESSO AO CRIAR A BASE DE DADOS =========================================")
    file.close()
    os.system('pause')


#FUNÇÕES PARA OCUPAR E DESOCUPAR VAGA:
def buscar_vaga_livre():
    placa_carro = input("DIGA A PLACA DO CARRO QUE IRÁ OCUPAR A VAGA: ")
    with open(v.arquivo2, 'a') as file2:
        with open(v.arquivo, 'r') as file:
            for linha in file:
                elementos = linha.strip().split(';')
                if len(elementos) == 2:
                    vaga = elementos[0]
                    verifica = buscar_vaga_ocupada_verifica(vaga)
                    estado = elementos[1]
                    if estado == "Livre" and verifica == False:
                        linha = linha.replace("Livre", placa_carro)
                        print(f"Sua vaga foi reservada.\nVAGA: {vaga}")
                        file2.write(linha)
                        os.system('pause')
                        return None 
    print("Estacionamento lotado")
    os.system('pause')

def desocupar_vaga():
    placa_carro = input("DIGA A PLACA DO CARRO QUE OCUPA A VAGA: ")
    with open(v.arquivo2, 'r') as file, open("arquivo_aux", 'w') as file_aux:
        vaga_desocupada = False
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 2:
                estado = elementos[1]
                if estado == placa_carro:
                    print("Vaga desocupada")
                    vaga_desocupada = True
                else:
                    file_aux.write(linha)
    if vaga_desocupada:
        os.replace("arquivo_aux", v.arquivo2)
    else:
        os.remove("arquivo_aux")

    os.system('pause')

    
def buscar_vaga_ocupada():
    placa_carro = input("DIGA A PLACA DO CARRO QUE OCUPA A VAGA: ")
    with open(v.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 2:
                vaga = elementos[0]
                estado = elementos[1]
                if estado == placa_carro:
                    print(f"Seu carro está aqui\nVAGA: {vaga}")
                    os.system('pause')
                    return None 
    print("Carro não encontrado")
    os.system('pause')


#FUNÇÕES DE EXIBIÇÃO DE INFORMAÇÕES: 
def exibir_funcionarios():
    os.system('cls')
    with open(f.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 4:
                nome = elementos[0]
                salario = elementos[1]
                id = elementos[2]
                cargo = elementos[3]
                print("============================================")
                print(f"NOME: {nome}\nID: {id}\nCARGO: {cargo}\nSALÁRIO: {salario}")
    file.close()
    os.system("pause")   

def exibir_clientes():
    os.system('cls')
    with open(c.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 3:
                nome = elementos[0]
                cpf = elementos[1]
                placa_carro = elementos[2]
                print("============================================")
                print(f"NOME: {nome}\nID: {id}\nCPF: {cpf}\nPLACA DO CARRO: {placa_carro}")
    file.close()
    os.system("pause")  

def exibir_vagas_ocupadas():
    os.system('cls')
    with open(v.arquivo2, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 2:
                nome = elementos[0]
                placa_carro = elementos[1]
                print("============================================")
                print(f"VAGA: {nome}\nPLACA DO CARRO: {placa_carro}")
    os.system("pause") 


#FUNÇÃO DE VERIFICAÇÃO:
def buscar_funcionario_sequencial_verifica(id_funcionario):
    with open(f.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 4:
                id = elementos[2]
                if str(id_funcionario) == id:
                    file.close()
                    return True
    file.close()
    return False

def buscar_funcionario_ordena_verifica(id_funcionario, arquivo):
    with open(arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 4:
                id = elementos[2]
                if str(id_funcionario) == id:
                    file.close()
                    return True
    file.close()
    return False

def buscar_vaga_ocupada_verifica(vaga):
    with open(v.arquivo2, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 2:
                vaga_ocupada = elementos[0]
                if str(vaga) == vaga_ocupada:
                    file.close()
                    return True
    file.close()
    return False


#FUNÇÕES DE BUSCA:
def buscar_funcionario_por_id(id_funcionario):
    with open(f.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 4:
                funcionario_id = int(elementos[2])
                if funcionario_id == id_funcionario:
                    nome = elementos[0]
                    salario = float(elementos[1])
                    cargo = elementos[3]
                    print(f"NOME: {nome}\nSALÁRIO: {salario}\nCARGO: {cargo}\nID: {funcionario_id}")
                    return None
    print("FUNCIONÁRRIO NÃO ENCONTRADO")
    return None

def buscar_cliente_por_cpf(cpf_cliente):
    with open(c.arquivo, 'r') as file:
        for linha in file:
            elementos = linha.strip().split(';')
            if len(elementos) == 3:
                cpf = elementos[2]
                if cpf == str(cpf_cliente):
                    nome = elementos[0]
                    placa_carro = elementos[1]
                    print(f"NOME: {nome}\nCPF: {cpf}\nPLACA DO CARRO: {placa_carro}\n")
                    return None
    print("CLIENTE NÃO ENCONTRADO")
    return None


#FUNÇÃO PARA ORDENAÇÃO:
def ordenar_funcionario():
    with open(f.arquivo, 'r') as file, open("arquivo_aux2", 'w+') as file_aux:
        quantidade_linhas = len(file.readlines())
        minimo = ["", 0, 9999999, ""]
        ids = []
        for i in range(quantidade_linhas):
            file.seek(0)  
            minimo[2] = 9999999
            for linha in file:
                elementos = linha.strip().split(';')
                if len(elementos) == 4:
                    id = elementos[2]
                    if id not in ids:
                        if int(id) < int(minimo[2]):
                            minimo = elementos
            ids.append(minimo[2])
            nova_linha = ';'.join(str(e) for e in minimo) + '\n'
            file_aux.write(nova_linha)
    os.replace("arquivo_aux2", f.arquivo)