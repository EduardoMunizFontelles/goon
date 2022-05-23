from Cadastro import cadastro
import os

def clean_console():
    os.system("cls")


#importar menuFuncionalidade()


continuar = input("Deseja realizar alguma consulta? [S] ou [N]: ")
while (continuar != 'N') and (continuar != 'S'):
    print("Resposta inválida")
    continuar = input("Deseja realizar alguma consulta? [S] ou [N]: ")

    while continuar == 'S':

        funcionalidade = int(input("Digite sua opcao: "))

        if funcionalidade == 1:
            clean_console()

            # Importar Funções de assistente virtual

            voltarParaMenu = input("Deseja voltar ao menu?[S] ou [N]: ")
            if voltarParaMenu == 'S':
                menuFuncionalidades()    
            else:
                continuar = 'N'

        elif funcionalidade == 2:
            clean_console()
            # importar funções emociometro

            resp = input("Deseja voltar ao menu? [S]: ")
            if resp == 'S':
                menuFuncionalidades()
            else:
                print("")
                clean_console()
            
        elif funcionalidade == 3:

            #calendário

        elif funcionalidade == 4:

            #Rendimento

        elif funcionalidade == 5:
            continuar = 'N'

        else:
            print("Erro. tente novamente.")

        