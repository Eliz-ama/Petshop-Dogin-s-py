from tkinter import* 
from tkinter import filedialog
from PIL import Image, ImageTk
ca=Tk()
import subprocess

taskBarHeight = 40

#Configurações da tela
ca.title("Acesso ao Petshop Dogin's")
ca.resizable(False, False)

width_screen = ca.winfo_screenwidth()
height_screen = ca.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

ca.maxsize(width, height)
ca.minsize(width, height)

ca.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
ca.configure(bg='#fff')

#Estilização do Logo
logodoginsorigin = Image.open("images/mainLogo.png")
logoresize = logodoginsorigin.resize((140, 50))
logoDogins = ImageTk.PhotoImage(logoresize)
logodog = Label(ca, image = logoDogins , bg="#fff")
logodog.place(relx = .150, rely = .10, anchor = "n")

#botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])
btn_menu = Button(ca, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777" , command=abrir_tela_menu)
btn_menu.place(relx = .830, rely = .10, anchor = "n")

#titulo dos serviços
txt_titulo = Label(ca,text="Cadastro do Pet" ,bg = "#FFF", font=("Helvetica 20 bold"))
txt_titulo.place(relx = .450, rely = .20, anchor = "n")
logo_cora= Image.open("images/heart-icon.png")
cora = logo_cora.resize((20, 15), Image.ANTIALIAS)
logo_coracao = ImageTk.PhotoImage(cora)
coracao = Label(ca, image = logo_coracao , bg="#fff")
coracao.place(relx = .575, rely = .21, anchor = "n")

#campo codigo do serviço
txt_codigo = Label(ca,text="Código do Cliente" ,bg = "#FFF", font=("Helvetica 10"))
txt_codigo.place(relx = .348, rely = .30, anchor = "n")
lbl_codigo = Entry(ca)
lbl_codigo.place(relx = .358, rely = .33, anchor = "n" ,  width="130" , height="20")

#campo nome
txt_nome = Label(ca,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .490, rely = .30, anchor = "n")
lbl_nome = Entry(ca)
lbl_nome.place(relx = .550, rely = .33, anchor = "n" ,  width="190" , height="20")

#campo data de nascimento
txt_duracao = Label(ca,text="Data de nascimento" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .353, rely = .40, anchor = "n")
lbl_duracao = Entry(ca)
lbl_duracao.place(relx = .353, rely = .43, anchor = "n",  width="120" , height="20")

#campo Idade
txt_duracao = Label(ca,text="Idade" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .440, rely = .40, anchor = "n")
lbl_duracao = Entry(ca)
lbl_duracao.place(relx = .460, rely = .43, anchor = "n",  width="80" , height="20")

#criando botao radio da especie
lbl_especie = Label(ca, text="Sexo", bg="#fff").place(relx = .530, rely = .40, anchor = "n")
var2=StringVar()
var2.set("c")
rdb_btn_c = Radiobutton(ca, text="Macho", variable=var2, value="c", bg="#fff")
rdb_btn_g = Radiobutton(ca, text="Femea", variable=var2, value="g", bg="#fff")
rdb_btn_c.place(relx = .540, rely = .43, anchor = "n")
rdb_btn_g.place(relx = .610, rely = .43, anchor = "n")

#campo Especie
txt_duracao = Label(ca,text="Espécie" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .325, rely = .50, anchor = "n")
lbl_duracao = Entry(ca)
lbl_duracao.place(relx = .338, rely = .53, anchor = "n",  width="80" , height="20")

#Raça
txt_descricao = Label(ca,text="Raça" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .423, rely = .50, anchor = "n")
lbl_descricao = Entry(ca)
lbl_descricao.place(relx = .453, rely = .53, anchor = "n" ,  width="120" , height="20")

#Peso
txt_descricao = Label(ca,text="Peso" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .543, rely = .50, anchor = "n")
lbl_descricao = Entry(ca)
lbl_descricao.place(relx = .563, rely = .53, anchor = "n" ,  width="90" , height="20")

#Descrição
txt_descricao = Label(ca,text="Descrição" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .330, rely = .58, anchor = "n")
lbl_descricao = Entry(ca)
lbl_descricao.place(relx = .465, rely = .61, anchor = "n" ,  width="400" , height="50")

#botões de salvar alterar e excluir
btn_salvar=Button(ca,text="Salvar", bg="#85d3ff")
btn_salvar.place(relx = .330, rely = .75, anchor = "n",  width="80" , height="25")
btn_alterar = Button(ca, text="Alterar")
btn_alterar.place(relx= .480, rely=.75, anchor= "n",  width="80" , height="25")
btn_excluir = Button(ca,text="Excluir")
btn_excluir.place(relx= .630, rely=.75 , anchor= "n",  width="80" , height="25")

# imagem e botao lateral pet
defaultPhoto = Image.open("images/defaultPhotoPet.png")
defaultPhotoSize = defaultPhoto.resize(( 170,200))
defaultProfilePhoto = ImageTk.PhotoImage(defaultPhotoSize)
defaultUploadLabel = Label(ca, image = defaultProfilePhoto)
defaultUploadLabel.place(relx = .15, rely = .45, anchor = "center")
#criar pasta para guardar imgs
pasta_inicial = ""

#função para escolher imagem
def escolher_imagem(): #inicio da função
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", ".jpg;.jpeg;*.png"),
                                                           ("Todos os arquivos", "."))) #localização do arquivo e tipos a serem utilizados
    imagem_pil = Image.open(caminho_imagem) #abertura do arquivo atraves do PIL
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura/150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura)) #redimensionamento da imagem
    imagem_tk = ImageTk.PhotoImage(imagem_pil) #convertendo a imagem para formato compativel com o Tkinter
    lbl_imagem = Label(ca, image=imagem_tk) 
    lbl_imagem = imagem_tk #a imagem escolhida será armaznada em uma label
    lbl_imagem.place(x="50" , y="50")

#botao chamando a função escolher_imagem
btn_escolher = Button(ca, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(relx = .15, rely = .620, anchor = "n")

#data de atualização
txt_descricao = Label(ca,text="Data de atualização" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .860, rely = .30, anchor = "n")
lbl_descricao = Entry(ca)
lbl_descricao.place(relx = .860, rely = .33, anchor = "n" ,  width="120" , height="20")

#Data de cadastro
txt_descricao = Label(ca,text="Data de cadastro" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .855, rely = .38, anchor = "n")
lbl_descricao = Entry(ca)
lbl_descricao.place(relx = .860, rely = .41, anchor = "n" ,  width="120" , height="20")

ca.mainloop()