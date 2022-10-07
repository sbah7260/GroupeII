from subprocess import call
from tkinter import *
from tkinter import ttk ,Entry
import customtkinter
from tkinter import ttk
from tkinter import messagebox


fenetre9 =Tk()
fenetre9.title("Les ventes ")
fenetre9.geometry("1000x620")
fenetre9.resizable(False, False)
fenetre9.configure(bg="white")
fenetre9.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\22926756.ico')

def retour():
    fenetre9.destroy()
    call(["python","accmag.py"])

texte =Label (fenetre9 ,text="Ventes" ,font=('Calistoga' ,25) ,bg="white")
texte.place(x=400 ,y=20 ,)
ret = Button(fenetre9, text="<<Retour", font=('Calistoga', 15), bg="#d9d9d9",command=retour)
ret.place(x=5, y='', )
def Action_bouton():
    VwIdVt.config(text=str(idchamp.get()))
    VwNomClt.config(text=str(nomchamp.get()))
    VwPrnmClt.config(text=str(prechamp.get()))
    VwTpProd.config(text=str(tprochamp.get()))
    VwAdr.config(text=str(adreschamp.get()))
    VwTelClt.config(text=str(telchamp.get()))


id = Label(fenetre9, text="Nom client" ,bg="#ffffff" ,fg="#000000")
id.place(x=50, y=80)

idchamp = Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
idchamp.place(x=160 ,y=80)

nom = Label(fenetre9, text="Type poduit" ,bg="#ffffff" ,fg="#000000")
nom.place(x=450, y=80)

nomchamp =Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
nomchamp.place(x=550 ,y=80 ,)

prenom = Label(fenetre9, text="Nom magasinier" ,bg="#ffffff" ,fg="#000000")
prenom.place(x=50, y=130)

prechamp =Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
prechamp.place(x=160 ,y=130 ,)

typro = Label(fenetre9, text="Quantité" ,bg="#ffffff" ,fg="#000000")
typro.place(x=450, y=130)

tprochamp =Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
tprochamp.place(x=550 ,y=130 ,)

adresse = Label(fenetre9, text="Nom du produit" ,bg="#ffffff" ,fg="#000000")
adresse.place(x=50, y=180)

adreschamp =Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
adreschamp.place(x=160 ,y=180 ,)

tel = Label(fenetre9, text="Prix" ,bg="#ffffff" ,fg="#000000")
tel.place(x=450, y=180)

telchamp =Entry(fenetre9 ,bg="white" ,width=25 ,font=('Calistoga' ,12))
telchamp.place(x=550 ,y=180 ,)

# les buton modification
pad= customtkinter.CTkButton(master=fenetre9 ,text="Valider" ,text_font=('Calistoga' ,11) ,command=Action_bouton,
                                      height=20 ,width=100 ,border_width=1 ,corner_radius=3 ,fg_color="#319BFE")
pad.place(x=640 ,y=220)
# facture

texte =Label (fenetre9 ,text="Facture" ,font=('Calistoga' ,17) ,bg="white")
texte.place(x=400 ,y=250 ,)

modif= customtkinter.CTkButton(master=fenetre9 ,text="Modifier" ,text_font=('Calistoga' ,11) ,command=quit,
                                      height=20 ,width=100 ,border_width=1 ,corner_radius=3 ,fg_color="#319BFE")
modif.place(x=200 ,y=590)
imp= customtkinter.CTkButton(master=fenetre9, text="Imprimer", text_font=('Calistoga', 11), command=quit,
                                      height=20, width=100, border_width=1, corner_radius=3, fg_color="#319BFE")
imp.place(x=600 ,y=590)
#
trai = Frame(fenetre9, bg='black', width="1000", height='1')
trai.place(x='',y='250')
trai = Frame(fenetre9, bg='black', width="800", height='1')
trai.place(x='100',y='280')

id = Label(fenetre9, text="Nom du client:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
id.place(x='', y=320)
VwIdVt = Label(fenetre9, width='15', height='2' ,bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwIdVt.place(x='200' ,y='310')
nom = Label(fenetre9, text="Type du poduit:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
nom.place(x='500', y=320)
VwNomClt = Label(fenetre9, width='15', height='2',bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwNomClt.place(x='700' ,y='310')
prenom = Label(fenetre9, text="Nom du magasinier:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
prenom.place(x='', y=400)
VwPrnmClt = Label(fenetre9, width='15', height='2',bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwPrnmClt.place(x='200' ,y='390')
typro = Label(fenetre9, text="Quantité:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
typro.place(x='500', y=400)
VwTpProd = Label(fenetre9, width='15', height='2',bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwTpProd.place(x='700' ,y='390')
adresse = Label(fenetre9, text="Nom du produit:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
adresse.place(x='', y=500)
VwAdr = Label(fenetre9, width='15', height='2',bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwAdr.place(x='200', y='490')
tel = Label(fenetre9, text="Prix:" ,bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
tel.place(x=500, y=500)
VwTelClt = Label(fenetre9, width='15', height='2',bg="#ffffff" ,fg="#000000", font=("times new roman", 15))
VwTelClt.place(x='700' ,y='490')

SignMAG = Label(fenetre9, text="Signature Du Client:", bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
SignMAG.place(x=650, y=550)
SignClt= Label(fenetre9, text="Signature Du Magasinier:", bg="#ffffff" ,fg="#000000",  font=("Calibri", 15))
SignClt.place(x=50, y=550)


fenetre9.mainloop()