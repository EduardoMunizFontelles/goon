
from Cadastro import cadastroAluno
from Login import loginAluno
from menu import printMenu
from AssistenteVirtual import *

botaoCadastroLogin = int(input("Cadastro-1, Login-2"))

while (botaoCadastroLogin != 1) and (botaoCadastroLogin != 2):
    if (botaoCadastroLogin == 1):
        cadastroAluno()
        loginAluno()
    elif(botaoCadastroLogin == 2):
        loginAluno()
    else:
        print("Erro. Digite 1 ou 2")       

botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2"))

while (botaoAssitenteEmociometro != 1) and (botaoAssitenteEmociometro != 2):
    if (botaoAssitenteEmociometro == 1):
        #assitenteVirtual()
    elif(botaoAssitenteEmociometro == 2):
        #emociometro()
    else:
        print("Erro. Digite 1 ou 2")


