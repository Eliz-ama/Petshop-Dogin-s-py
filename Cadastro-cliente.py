from tkinter import*
from PIL import Image, ImageTk
cc=Tk()
import subprocess
taskBarHeight = 40

#Configurações da tela
cc.title("Acesso ao Petshop Dogin's")
cc.resizable(False, False)

width_screen = cc.winfo_screenwidth()
height_screen = cc.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

cc.maxsize(width, height)
cc.minsize(width, height)

cc.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
cc.configure(bg='#fff')

#Estilização do Logo
logodoginsorigin = Image.open("images/mainLogo.png")
logoresize = logodoginsorigin.resize((140, 50))
logoDogins = ImageTk.PhotoImage(logoresize)
logodog = Label(cc, image = logoDogins , bg="#fff")
logodog.place(relx = .150, rely = .10, anchor = "n")

#botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])
btn_menu = Button(cc, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777" , command=abrir_tela_menu)
btn_menu.place(relx = .830, rely = .10, anchor = "n")

#titulo dos serviços
txt_titulo = Label(cc,text="Cadastro do Cliente" ,bg = "#FFF", font=("Helvetica 20 bold"))
txt_titulo.place(relx = .450, rely = .20, anchor = "n")
logo_cora= Image.open("images/heart-icon.png")
cora = logo_cora.resize((20, 15), Image.ANTIALIAS)
logo_coracao = ImageTk.PhotoImage(cora)
coracao = Label(cc, image = logo_coracao , bg="#fff")
coracao.place(relx = .585, rely = .21, anchor = "n")

#campo codigo do serviço
txt_codigo = Label(cc,text="Código do Cliente" ,bg = "#FFF", font=("Helvetica 10"))
txt_codigo.place(relx = .350, rely = .30, anchor = "n")
lbl_codigo = Entry(cc)
lbl_codigo.place(relx = .360, rely = .33, anchor = "n" ,  width="130" , height="20")

#campo nome
txt_nome = Label(cc,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .500, rely = .30, anchor = "n")
lbl_nome = Entry(cc)
lbl_nome.place(relx = .560, rely = .33, anchor = "n" ,  width="190" , height="20")

#campo cpf
txt_valor = Label(cc,text="CPF" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .317, rely = .40, anchor = "n")
lbl_valor = Entry(cc)
lbl_valor.place(relx = .342, rely = .43, anchor = "n",  width="90" , height="20")

#campo data de nascimento
txt_duracao = Label(cc,text="Data de nascimento" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .470, rely = .40, anchor = "n")
lbl_duracao = Entry(cc)
lbl_duracao.place(relx = .470, rely = .43, anchor = "n",  width="120" , height="20")

#campo Idade
txt_duracao = Label(cc,text="Idade" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .560, rely = .40, anchor = "n")
lbl_duracao = Entry(cc)
lbl_duracao.place(relx = .580, rely = .43, anchor = "n",  width="80" , height="20")

#Celular
txt_descricao = Label(cc,text="Celular" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .325, rely = .49, anchor = "n")
lbl_descricao = Entry(cc)
lbl_descricao.place(relx = .355, rely = .52, anchor = "n" ,  width="120" , height="20")

#campo cep
txt_valor = Label(cc,text="Cep" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .317, rely = .56, anchor = "n")
lbl_valor = Entry(cc)
lbl_valor.place(relx = .342, rely = .59, anchor = "n",  width="90" , height="20")

#campo endereço
txt_nome = Label(cc,text="Endereço" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .449, rely = .56, anchor = "n")
lbl_nome = Entry(cc)
lbl_nome.place(relx = .500, rely = .59, anchor = "n" ,  width="190" , height="20")

#campo numero
txt_valor = Label(cc,text="N°" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .593, rely = .56, anchor = "n")
lbl_valor = Entry(cc)
lbl_valor.place(relx = .600, rely = .59, anchor = "n",  width="30" , height="20")

#campo bairro
txt_valor = Label(cc,text="Bairro" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .320, rely = .63, anchor = "n")
lbl_valor = Entry(cc)
lbl_valor.place(relx = .365, rely = .66, anchor = "n",  width="150" , height="20")

#campo cidade
txt_nome = Label(cc,text="Cidade" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .467, rely = .63, anchor = "n")
lbl_nome = Entry(cc)
lbl_nome.place(relx = .500, rely = .66, anchor = "n" ,  width="120" , height="20")

#campo cidade
txt_nome = Label(cc,text="UF" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .574, rely = .63, anchor = "n")
lbl_nome = Entry(cc)
lbl_nome.place(relx = .580, rely = .66, anchor = "n" ,  width="30" , height="20")

#botões de salvar alterar e excluir
btn_salvar=Button(cc,text="Salvar", bg="#85d3ff")
btn_salvar.place(relx = .330, rely = .75, anchor = "n",  width="80" , height="25")
btn_alterar = Button(cc, text="Alterar")
btn_alterar.place(relx= .480, rely=.75, anchor= "n",  width="80" , height="25")
btn_excluir = Button(cc,text="Excluir")
btn_excluir.place(relx= .630, rely=.75 , anchor= "n",  width="80" , height="25")

cc.mainloop()