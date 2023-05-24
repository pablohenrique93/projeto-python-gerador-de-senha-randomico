# ---------------------------------------------------------------- GERADOR DE SENHAS -----------------------------------------------------------

# Importação de Biblioteca
from tkinter import *
# Importação da Bilioteca para utilizar estilos
from tkinter import ttk
# Importação da Biblioteca para aparição de mensagem na tela
from tkinter import messagebox 
# Importação da Biblioteca Pillow para utilização de imagens
from PIL import ImageTk, Image
# Importação de Biblioteca para utilização de letras Maiúsculas nos opcionais
import string
# Importação da biblioteca randômica, pois as senhas serão geradas de forma aleatória
import random


# Primeiras Definições
# Definição de cores que vão ser utilizadas no projeto

cor0 = '#444466' # Cor Preta
cor1 = '#feffff' # Cor Branca
cor2 = '#f05a43' # Cor Vermelha

# Definição da janela

janela = Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor1)

# Definição do Estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam') 

# Criação dos Frames
# Dividindo a tela em dois frames
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Definição de estilo
# Trabalhando no Frame CIMA
img = Image.open('D:\Biblioteca\Downloads\projetos python\senha.png') # Utilizando a imagem que se encontra o mesmo diretório
img = img.resize((30, 30), Image.ANTIALIAS) # Definição do tamanho da imagem
img = ImageTk.PhotoImage(img)

# Criação do Label 1 (ícone/imagem)
 
app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=3) # Posicionando o logo no frame cima

# Criação do Label 2 (Nome)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Lato 16 bold'), bg=cor1, fg=cor0)
app_nome.place(x=45, y=5)

# Criação da Linha abaixo do nome do Aplicativo

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Lato 1'), bg=cor2, fg=cor0)
app_linha.place(x=0, y=40)


# ------------------------------------ Criação da Função do Aplicativo (Gerar Senha) -----------------------------------------

def criar_senha():
    alfabeto_maior = string.ascii_uppercase # variável para alfabeto maiúsculo
    alfabeto_menor = string.ascii_lowercase # variável para alfabeto minúsculo
    numeros = '123456789' # variável para números
    simbolos = '[]{}()*;/,_-' # variável para símbolos

    # Criação da variável que irá conter todos os caracteres gerados, 
    # essa variável irá conter um "mix" de todas os caracteres acima
    global combinar 
    
    # ----- Condição para maiúscula
    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        pass

    # ----- Condição para minúscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

    # ----- Condição para número
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # ----- Condição para símbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    

# Criação da variável contendo o "random" para gerar a senha de forma aleatória
    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    # Criação de função do botão "Copiar"
    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso!")

    botao_copiar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar', width=7, height=2, relief='raised', overrelief='solid', anchor='center', font=('Lato 10 bold'), bg=cor1, fg=cor0)
    botao_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1) 

   

# Trabalhando no frame BAIXO
# Criação de Label de exibição da senha gerada

app_senha = Label(frame_baixo, text='- - - - -', width=21, height=2, padx=0, relief='solid', anchor='center', font=('Lato 12 bold'), bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

# Criação da Opção: "Número total de caracteres"

app_info = Label(frame_baixo, text='Número Total de Caracteres na Senha', height=1, padx=0, relief='flat', anchor='nw', font=('Lato 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

# Criação do 'Spin Box', ou seja, o campo de seleção de número de caracteres
var = IntVar()
var.set(8) # Definindo Valor Inicial
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)


# Criação dos Frames contendo informações dos opcionais para serem inclusos ou não para gerar as senhas

alfabeto_maior = string.ascii_uppercase # variável para alfabeto maiúsculo
alfabeto_menor = string.ascii_lowercase # variável para alfabeto minúsculo
numeros = '123456789' # variável para números
simbolos = '[]{}()*;/,_-' # variavel para símbolos


frame_caracteres = Frame(frame_baixo, width=280, height=210, bg=cor1, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)


# ------------------------------------- Criação do Check Button -------------------------------------------
# Letras Maiúsculas
estado_1 = StringVar() # Opção que irá mostrar se o botão está marcado ou não
estado_1.set(False)  
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
# Criação da Descrição do opcional
app_info = Label(frame_caracteres, text='ABC Letras Maiúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Lato 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5) 

# Letras Minúsculas
estado_2 = StringVar() # Opção que irá mostrar se o botão está marcado ou não
estado_2.set(False)  
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
# Criação da Descrição do opcional
app_info = Label(frame_caracteres, text='abc Letras Minúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Lato 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# Números
estado_3 = StringVar() # Opção que irá mostrar se o botão está marcado ou não
estado_3.set(False)  
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
# Criação da Descrição do opcional
app_info = Label(frame_caracteres, text='123 Números', height=1, padx=0, relief='flat', anchor='nw', font=('Lato 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5) 

# Símbolos
estado_4 = StringVar() # Opção que irá mostrar se o botão está marcado ou não
estado_4.set(False)  
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor1)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
# Criação da Descrição do opcional
app_info = Label(frame_caracteres, text='[]{}()*;/... Símbolos', height=1, padx=0, relief='flat', anchor='nw', font=('Lato 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5) 


# ------------------------------------ Criação dos Botões "Gerar Senha" e "Copiar"  ---------------------------------------

botao_gerar_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=34, height=1, relief='flat', overrelief='solid', anchor='center', font=('Lato 10 bold'), bg=cor2, fg=cor1)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=10, columnspan=5) 


janela.mainloop()
