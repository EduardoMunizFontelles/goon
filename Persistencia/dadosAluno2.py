import csv

with open('dadosAluno.csv', encoding='utf-8') as arquivo:

    write = csv.writer(arquivo, delimiter=';')
    cabecalho = ['Nome', 'Notas', 'Ajuda', 'Login', 'Senha']
    write.writerow(cabecalho)

    aluno1 = ['Eduardo Muniz Fontelles', '9', 'Assitente Virtual', 'Ed', "4275"]
    write.writerow(aluno1)
    aluno2 = ['Jão Muniz Fontelles', '3', 'Assitente Virtual', 'JF', "0275"]
    write.writerow(aluno2)
    aluno3 = ['Luiz Muniz Fontelles', '6', 'Assitente Virtual', 'HG', "0265"]
    write.writerow(aluno3)
    
