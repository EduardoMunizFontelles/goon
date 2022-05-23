from tkinter import *
from tkinter import messagebox
import csv
import time
import os
def lim():
    os.system('cls')

dados = []

#Definindo as cores
co0 = "#fof3f5" # preto
co1 = "#feffff" # branco
co2 = "#3fb5a3" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra

#criando janela ------------------------------

janela = Tk()
janela.title("Portal do Aluno")
janela.geometry("310x300")
janela.configure(background=co1)

#dividindo janela ------------------------------


frame_cima = Frame(janela,width=310,height=50,bg=co1,relief="flat")
frame_cima.grid(row=0,column=0,padx=1, sticky=NSEW)

frame_baixo = Frame(janela,width=310,height=250,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,padx=1, sticky=NSEW)

#configurando o frame de cima ------------------------------
L1 = Label(frame_cima, text='LOGIN',anchor=NE,font=('Calibri 25'), bg =co1,fg = co4)
L1.place(x=5,y=5)

Linha1 = Label (frame_cima, text="",width=275,anchor=NW,font=('ily 1'), bg = co2)
Linha1.place(x=10,y=45)

credenciais = ['Falk','1234', 'Adaury', '1234', 'Lara', '1234', 'Geraldo', '1234' , 'Caio' , '1234' ,'Walter' , '1234']

def verificar_senha():
    nome = E_nome.get()
    senha = E_senha.get()

    if nome == credenciais [0] and senha == credenciais [1] or nome == credenciais [2] \
and senha == credenciais [3] or nome == credenciais [4] and senha == credenciais [5] or nome == credenciais [6] and senha == credenciais [7]:
     messagebox.showinfo(message="LOGIN CONFIRMADO.")
     time.sleep(0.5)
     messagebox.showinfo(message=f"Seja bem vindo {nome}.")
     dados.append(nome)

    else:
        messagebox.showwarning(message='ERRO.') 
        time.sleep(0.5)
        messagebox.showwarning(message='Verifique a senha e o nome.')

#configurando o frame de baixo ------------------------------
L_nome1 = Label(frame_baixo, text='Nome *',anchor=NW,font=('ily 10'), bg =co1,fg = co4)
L_nome1.place(x=14,y=20)

E_nome = Entry(frame_baixo,width=25,justify='left',font=("",13),highlightthickness=1,relief='solid',)
E_nome.place(x=14,y=50)

L_nome1 = Label(frame_baixo, text='Senha *',anchor=NW,font=('ily 10'), bg =co1,fg = co4)
L_nome1.place(x=14,y=100)

E_senha = Entry(frame_baixo,width=25,justify='left',font=("",13),highlightthickness=1,relief='solid',)
E_senha.place(x=14,y=130)

b_confirmar = Button(frame_baixo,text='ENTRAR',command= verificar_senha,width=39,height=2,font="ily 8 bold",bg=co2,fg=co1,relief=RAISED)
b_confirmar.place(x=14,y=180)


janela.mainloop()

codigoAula = "MA0000"
comentarios = []
codigo = input("Digite o código : ")
validos = ['0','1','2','3','4','5']
lim()
while codigo != codigoAula :
    print("Código de Aula não encontrado\n ")
    codigo = input("Digite o codigo : ")

d1 = input("O quanto você entendeu do assunto da aula [0 - 5]")
v = True
while v:
    v = d1 not in validos
    if v:
        print("Resposta inválida")
        d1 = input("O quanto você entendeu do assunto da aula [0 - 5]")
lim()

d2 = input("Você gostou da maneira como a aula foi dada ? [0 - 5]")
v = True
while v:
    v = d2 not in validos
    if v:
        print("Resposta inválida")
        d2 = input("Você gostou da maneira como a aula foi dada ? [0 - 5]")
lim()

d3 = input("O assunto foi dado com clareza ? [0 - 5]")
v = True
while v:
    v = d3 not in validos
    if v:
        print("Resposta inválida")
        d3 = input("O assunto foi dado com clareza ? [0 - 5]")

lim()
d4 = input("Algum comentário da aula ? ")

lim()

if dados[0] == 'Falk':
    def Anotar(Arquivo, lista) :
        with open(Arquivo,'a') as arq :
            data = ','.join(lista)
            arq.writelines(data+'\n')

    with open('turmaB.csv','r') as adm:
        leitor = csv.reader(adm,delimiter='\n')

    dados.append(d1)
    dados.append(d2)
    dados.append(d3)
    dados.append(d4)

    Anotar('turmaB.csv', dados)
else:
    def Anotar(Arquivo, lista) :
        with open(Arquivo,'a') as arq :
            data = ','.join(lista)
            arq.writelines(data+'\n')

    with open('turmaA.csv','r') as adm:
        leitor = csv.reader(adm,delimiter='\n')

    dados.append(d1)
    dados.append(d2)
    dados.append(d3)
    dados.append(d4)

    Anotar('turmaA.csv', dados)
