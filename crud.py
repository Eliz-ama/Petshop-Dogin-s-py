from tkinter import *
from PIL import Image, ImageTk
import subprocess
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import cv2
import numpy as np
import tkinter as tk

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

logodoginsorigin = Image.open("images/mainLogo.png")
logoresize = logodoginsorigin.resize((140, 50))
logoDogins = ImageTk.PhotoImage(logoresize)
logodog = Label(crud, image = logoDogins , bg="#fff")
logodog.place(relx = .150, rely = .10, anchor = "n")

lbl_nome = Label(crud, text="Nome", font=("Arial 12"))
lbl_nome.place(relx=0.37,rely=0.3)
txt_nome= Entry(crud, font=("Aial 12"))
txt_nome.place(relx=0.43 , rely=0.3)

lbl_cpf=Label(crud,text="CPF:", font=("Arial 12"))
lbl_cpf.place(relx=0.37,rely=0.4)
txt_cpf=Entry(crud, font=("Arial 12"))
txt_cpf.place(relx=0.43, rely=0.4)

lbl_email=Label(crud,text="E-mail:", font=("Arial 12"))
lbl_email.place(relx=0.37,rely=0.5)
txt_email = Entry(crud, font=("Arial 12"))
txt_email.place(relx=0.43,rely=0.5)

def salvar():
    variavel_nome= txt_nome.get()
    variavel_cpf = txt_cpf.get()
    variavel_email = txt_email.get()

    if(variavel_nome == "" or variavel_cpf == "" or variavel_email==""):
        MessageBox.showinfo("Erro","Há campos em branco")
    else:

        conectar = mysql.connect(host="localhost",user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("insert into promocao values('"+ variavel_nome + "','"+ variavel_email + "','"+ variavel_cpf + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem","Cadastro realizado com sucesso")
        conectar.close()

def excluir():
    if(txt_nome.get() == ""):
        MessageBox.showinfo("ALERT" , "Digite o código para deletar")
    else:
        conectar= mysql.connect(host="localhost", user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("delete from promocao where cpf='"+txt_cpf.get() + "'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação excluída com sucesso")
        crud.close()

def atualizar():
    id = txt_nome.get()
    name = txt_nome.get()
    cpf = txt_cpf.get()
    if(name == "" or cpf == ""):
        MessageBox.showinfo("ALERT" , "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connect(host="localhost", user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("Update promocao set nome = '"+ txt_nome.get() +"', email='"+ txt_email.get() + "'where cpf = '"+ txt_cpf.get()+"'")
        cursor.execute("commit");
        MessageBox.showinfo("status","Successfully Update")
        conectar.close()

def Select():
    if(txt_cpf.get() == ""):
        MessageBox.showinfo("ALERT","Por favor digite o código")
    else:
        conectar = mysql.connect(host="localhost",user="root", password="",database="crud")
        cursor = conectar.cursor()
        cursor.execute("select * from promocao where cpf= '" + txt_cpf.get()+"'")
        rows = cursor.fetchall()
        for row in rows:
            txt_nome.insert(0, row[0])
            txt_email.insert(0, row[1])
        conectar.close()
txt_mensagem = Label(crud, text="Faça seu cadastro para receber promoções exclusivas",font=("Arial 18"))
txt_mensagem.place(relx=0.25,rely=0.2)

btn_salvar = Button(crud, text="Salvar", command=salvar, font="Arial 12",  bg = "#85d3ff").place(relx=0.26,rely=0.7)
btn_excluir = Button(crud, text="Apagar", command=excluir, font="Arial 12", bg = "#85d3ff").place(relx=0.36, rely=0.7)
btn_update = Button(crud, text="Update", command=atualizar, font="Arial 12",bg = "#85d3ff").place(relx=0.46, rely=0.7)
btn_consultar = Button(crud, text="Consultar", command=Select, font="Arial 12",bg = "#85d3ff").place(relx=0.56, rely=0.7)
btn_img = Button(crud, text="Selecione uma imagem", command=lambda:abrir_tela_rotate(), font="Arial 12",bg = "#85d3ff").place(relx=0.66, rely=0.7)

def abrir_tela_rotate():
    subprocess.run(["python", "rotateImg.py"])

# Executar a interface gráfica Tkinter
crud.mainloop()
