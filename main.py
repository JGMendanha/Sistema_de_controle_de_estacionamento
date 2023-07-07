import Funcionario as f
import funcoes as o
import interface as i
import os

if os.path.exists("Funcionario.txt"):  
    o.direcionamento_de_interface()
else:
    print("===================================== BEM VINDO AO SISTEMA DE CONTROLE DE ESTACIONAMENTO =====================================")
    print("\t\t\t\tPARA INICIAR SEU SISTEMA VAMOS COMEÇAR CRIANDO UM ADMINISTRADOR\n\t\t\t\t     SEM ELE, AS PRÓXIMAS OPERAÇÕES NÃO PODEM SER REALIZADAS")
    o.cadastrar_adm()
    print("========================================= SUCESSO AO CRIAR O PRIMEIRO ADIMINISTRADOR =========================================")
    os.system('pause')
    o.direcionamento_de_interface()
