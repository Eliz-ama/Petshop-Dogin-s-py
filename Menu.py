from tkinter import*
from PIL import Image, ImageTk
import subprocess
me=Tk()

taskBarHeight = 40

#Configurações da tela
me.title("Acesso ao Petshop Dogin's")
me.resizable(False, False)

width_screen = me.winfo_screenwidth()
height_screen = me.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

me.maxsize(width, height)
me.minsize(width, height)

me.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
me.configure(bg='#fff')

#barra de menu
largura = 1000
altura = 700

barra_menu = Menu(me)

opcoes_menu_arquivo = Menu(barra_menu)
opcoes_menu_gestao = Menu(barra_menu)

barra_menu.add_cascade(label="Arquivo" , menu=opcoes_menu_arquivo)
barra_menu.add_cascade(label="Gestão" , menu=opcoes_menu_gestao)

opcoes_menu_arquivo.add_command(label="Abrir")
opcoes_menu_arquivo.add_command(label="Salvar")
opcoes_menu_arquivo.add_command(label="Salvar como ...")
opcoes_menu_arquivo.add_separator()
opcoes_menu_arquivo.add_command(label="Sair" , command=me.quit)

opcoes_novo = Menu(opcoes_menu_arquivo)

opcoes_menu_arquivo.add_cascade(label="Novo" , menu=opcoes_novo)
opcoes_menu_arquivo.add_command(label="Abrir")


opcoes_novo.add_command(label="Salvar Imagem")
opcoes_novo.add_command(label="Upload Arquivos")

me.config(menu=barra_menu)

#Estilização do Logo
logo_dogins_origin = Image.open("images/mainLogo.png")
logo_resize = logo_dogins_origin.resize((140, 50), Image.ANTIALIAS)
logoDogins = ImageTk.PhotoImage(logo_resize)
logo_dog = Label(me, image = logoDogins , bg="#fff")
logo_dog.place(relx = .150, rely = .10, anchor = "n")


foto_sair = PhotoImage(file =r"images/sair.png")
foto_animais = PhotoImage(file =r"images/animal.png")
foto_usuario = PhotoImage(file =r"images/usuario.png")
foto_serviços = PhotoImage(file =r"images/servico.png")
foto_logout = PhotoImage(file =r"images/sair.png")

btn_animais = Button(me, text="Animais",image=foto_animais,compound = TOP).place(relx=.35 , rely=.20 , width="150" , height="150" )
btn_Clientes = Button(me, text="Clientes",image=foto_usuario,compound = TOP).place(relx=.55 , rely=.20 ,width="150" , height="150" )
btn_Serviços = Button(me, text="Serviços",image=foto_serviços,compound = TOP).place(relx=.35 , rely=.50, width="150" , height="150" )
btn_logout = Button(me, text="Logout",image=foto_logout,compound = TOP).place(relx=.55 , rely=.50 ,width="150" , height="150" )

def abrir_tela_animais():
    subprocess.run(["python", "cadastro-animal.py"])
def abrir_tela_clientes():
    subprocess.run(["python", "cadastro-cliente.py"])
def abrir_tela_servicos():
    subprocess.run(["python", "cadastro-servico.py"])
def abrir_tela_op():
    subprocess.run(["python", "operação-concluida.py"])
def abrir_tela_crud():
    subprocess.run(["python", "crud.py"])
                    
opcoes_menu_gestao.add_command(label="Animais", command=abrir_tela_animais)
opcoes_menu_gestao.add_command(label="Clientes", command=abrir_tela_clientes)
opcoes_menu_gestao.add_command(label="Serviços", command=abrir_tela_servicos)
opcoes_menu_gestao.add_command(label="Operação concluida" , command=abrir_tela_op)
opcoes_menu_gestao.add_command(label="Cadastro de Promoções" , command=abrir_tela_crud)


me.title("Pet shop Dogin's")

me.mainloop()