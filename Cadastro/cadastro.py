from Login import login

def cadastroAluno():


    nome = input("Digite o seu nome completo: ")
    idade = int(input("Digite a sua idade: "))
    login = nome
    senha = input("Digite a sua senha: ")
    confSenha = input("Confirme a sua senha: ")

    while (senha != confSenha):
        confSenha = input("Confirme a sua senha: ")

    with open("dadosAlunos.txt", "w") as arquivoDadosAlunos:
        #escrever os dados

    login()

    # Salvar esses dados no DB
    # Depois do cadastro vai para a teal do login     