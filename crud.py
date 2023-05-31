from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import mysql.connector

crud=Tk()

#Configurações da tela
taskBarHeight = 40
crud.title("Acesso ao Petshop Dogin's")
crud.resizable(False, False)

width_screen = crud.winfo_screenwidth()
height_screen = crud.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

crud.maxsize(width, height)
crud.minsize(width, height)

crud.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
crud.configure(bg='#fff')

# lbl_id = Entry(crud)
# lbl_id.place(relx=.300, rely=.8, anchor="n", width="100", height="25")

# Conectando ao banco de dados
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='crud'
)

# Função para criar um registro
def create_record(nome, email, cpf):
    cursor = cnx.cursor()
    query = "INSERT INTO promocao (nome, email, cpf) VALUES (%s, %s, %s)"
    values = (nome, email, cpf)
    cursor.execute(query, values)
    cnx.commit()
    messagebox.showinfo("Sucesso", "Registro cadastrado com sucesso!")
    cursor.close() 

# Função para ler todos os registros
def read_records():
    cursor = cnx.cursor()
    query = "SELECT * FROM promocao"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    return records

# Função para atualizar um registro
def update_record(nome, email, cpf):
    cursor = cnx.cursor()
    query = "UPDATE promocao SET nome = %s, email = %s WHERE cpf = %s"
    values = (nome, email, cpf)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()

# Função para deletar um registro
def delete_record(cpf):
    cursor = cnx.cursor()
    query = "DELETE FROM promocao WHERE cpf = %s"
    values = (cpf)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()

#Estilização do Logo
logodoginsorigin = Image.open("images/mainLogo.png")
logoresize = logodoginsorigin.resize((140, 50))
logoDogins = ImageTk.PhotoImage(logoresize)
logodog = Label(crud, image = logoDogins , bg="#fff")
logodog.place(relx = .150, rely = .10, anchor = "n")

#campo nome
txt_promo = Label(crud,text="Se cadastrando aqui, você receberá promoções exclusivas" ,bg = "#FFF", font=("Helvetica 15"))
txt_promo.place(relx = .500, rely = .15, anchor = "n")

#campo nome
txt_nome = Label(crud,text="Nome" ,bg = "#FFF", font=("Helvetica 15"))
txt_nome.place(relx = .500, rely = .30 , anchor = "n")
lbl_nome = Entry(crud)
lbl_nome.place(relx = .500, rely = .34, anchor = "n" ,  width="190" , height="20")

#campo email
txt_email = Label(crud,text="Email" ,bg = "#FFF", font=("Helvetica 15"))
txt_email.place(relx = .500, rely = .44, anchor = "n")
lbl_email= Entry(crud)
lbl_email.place(relx = .500, rely = .48, anchor = "n" ,  width="190" , height="20")

#campo cpf
txt_cpf = Label(crud,text="CPF" ,bg = "#FFF", font=("Helvetica 15"))
txt_cpf.place(relx = .500, rely = .60, anchor = "n")
lbl_cpf = Entry(crud)
lbl_cpf.place(relx = .500, rely = .64, anchor = "n" ,  width="190" , height="20")

botao = Button(crud, text="Enviar", command=lambda:create_record(lbl_nome.get(), lbl_email.get(), lbl_cpf.get()))
botao.place(relx=.400, rely=.8, anchor="n",  width="100" , height="25")

botaoAtualizar = Button(crud, text="Atualizar", command=lambda:update_record(lbl_nome.get(), lbl_email.get(), lbl_cpf.get()))
botaoAtualizar.place(relx=.500, rely=.8, anchor="n", width="100", height="25")

botaoExcluir = Button(crud, text="Excluir", command=lambda:delete_record(lbl_cpf.get()))
botaoExcluir.place(relx=.600, rely=.8, anchor="n", width="100", height="25")

botaoVisualizar = Button(crud, text="Visualizar", command=read_records)
botaoVisualizar.place(relx=.700, rely=.8, anchor="n", width="100", height="25")


crud.mainloop()