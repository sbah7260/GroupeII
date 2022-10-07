
# page fournisseur admin
from subprocess import call
from tkinter import *
from tkinter import Entry
import customtkinter as customtkinter
from tkinter import ttk
import pymysql as pymysql

from tkinter import messagebox



def retour():
    fenetre6.destroy()
    call(["python","accadmin.py"])


fenetre6 =Tk()
fenetre6.title("Fourniseur ")
fenetre6.geometry("1000x620")
fenetre6.resizable(False, False)
fenetre6.configure(bg="white")
fenetre6.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\22926756.ico')

# affichage resultat
aff= ttk.Treeview(fenetre6, columns=(1 ,2 ,3 ,4 ,5 ,6) ,height=10 ,show="headings")
aff.place(x='' ,y='290' ,width=1000 ,height=280)


# nouveau fonction

def callback(event):
    ligne_id = aff.selection()[0]
    selection = aff.set(ligne_id)


    if selection:
        idchamp.delete(0, END)
        idchamp.insert(0, selection['1'])
        nomchamp.delete(0, END)
        nomchamp.insert(0, selection['2'])
        prechamp.delete(0, END)
        prechamp.insert(0, selection['3'])
        typrochamp.delete(0, END)
        typrochamp.insert(0, selection['4'])
        adreschamp.delete(0, END)
        adreschamp.insert(0, selection['5'])
        telchamp.delete(0, END)
        telchamp.insert(0, selection['6'])
       # idchamp.set(selection['2'])

        print(selection)
    else:
        print('nnnn')

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor =con.cursor()
    cursor.execute("select * from four ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id ,nom ,prenom ,tel ,typro ,adresse) in enumerate (records ,start=1):
            aff.insert ("", "end", values=(id ,nom ,prenom ,tel ,typro ,adresse))

    con.close()

afficher()


# les fonctions


def recuperer():
    id = idchamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("select * from four where id='" + idchamp.get() + "'")
    rows = cursor.fetchall()
    cursor.execute("commit")

    idchamp.delete(0, "end")
    for row in rows:
        idchamp.insert(0, row[0])
        nomchamp.insert(0, row[1])
        prechamp.insert(0, row[2])
        telchamp.insert(0, row[3])
        adreschamp.insert(0, row[5])
        typrochamp.insert(0, row[4])
    afficher()
    con.close()
def ajouter():
    id = idchamp.get()
    nom = nomchamp.get()
    prenom = prechamp.get()
    tel = telchamp.get()
    typro = typrochamp.get()
    adresse = adreschamp.get()

    if (id == " " or nom == " " or prenom == " " or tel == " " or typro == " " or adresse == " "):
        messagebox.showinfo("Message d'erreur", "Tout les champs sont requis")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute \
            ("insert into four values('" + id + "','" + nom + "','" + prenom + "','" + tel + "','" + typro + "','" + adresse + "') ")
        cursor.execute("commit")

    idchamp.delete(0 ,"end")
    nomchamp.delete(0 ,"end")
    prechamp.delete(0 ,"end")
    telchamp.delete(0 ,"end")
    adreschamp.delete(0 ,"end")
    typrochamp.delete(0 ,"end")
    afficher()

    con.close()


def supprimer():
    if (idchamp.get() == " " ):
        messagebox.showinfo("Message d'erreur", "Inserer l'ID");
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute("delete from four where id='" + idchamp.get() + "' ")
        cursor.execute("commit")
        afficher()
        con.close()

    idchamp.delete(0, "end")
    nomchamp.delete(0, "end")
    prechamp.delete(0, "end")
    telchamp.delete(0, "end")
    adreschamp.delete(0, "end")
    typrochamp.delete(0, "end")
    afficher()


def modifier():
    id = idchamp.get()
    nom = nomchamp.get()
    prenom = prechamp.get()
    tel = telchamp.get()
    typro = typrochamp.get()
    adresse =adreschamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute \
        ("update four set id=' " +id +"',nom='" + nom + "',prenom='" + prenom + "',tel='" + tel + "',typro='" + typro + "',adresse='" + adresse + "' where id='" + id + " '")
    cursor.execute("commit")

    idchamp.delete(0, "end")
    nomchamp.delete(0, "end")
    prechamp.delete(0, "end")
    telchamp.delete(0, "end")
    adreschamp.delete(0, "end")
    typrochamp.delete(0, "end")

    afficher()
    con.close()

def recherche():
    padchamp.get()


    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("select * from four where tel='" + padchamp.get() + "'")
    # cursor.execute("select * from fournisseur where id='" + padchamp.get() + "'")
    rows = cursor.fetchall()
    cursor.execute("commit")

    padchamp.delete(0, "end")
    for row in rows:
        idchamp.insert(0, row[0])
        nomchamp.insert(0, row[1])
        prechamp.insert(0, row[2])
        telchamp.insert(0, row[3])
        adreschamp.insert(0, row[5])
        typrochamp.insert(0, row[4])

        padchamp.delete(0, "end")

    con.close()


texte = Label(fenetre6, text="Fournisseurs", font=('Calistoga', 25), bg="white")
texte.place(x=400, y='', )
ret = Button(fenetre6, text="<<Retour", font=('Calistoga', 15), bg="#d9d9d9",command=retour)
ret.place(x=5, y='', )

id = Label(fenetre6, text="ID", bg="#ffffff", fg="#000000").place(x=140, y=80)

idchamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
idchamp.place(x=140, y=100, )

nom = Label(fenetre6, text="Nom", bg="#ffffff", fg="#000000").place(x=140, y=130)

nomchamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
nomchamp.place(x=140, y=150, )

prenom = Label(fenetre6, text="Prénom", bg="#ffffff", fg="#000000").place(x=140, y=180)

prechamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
prechamp.place(x=140, y=210, )

typro = Label(fenetre6, text="Type de produit", bg="#ffffff", fg="#000000").place(x=500, y=80)

typrochamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
typrochamp.place(x=500, y=100, )

adresse = Label(fenetre6, text="Adresse", bg="#ffffff", fg="#000000").place(x=500, y=130)

adreschamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
adreschamp.place(x=500, y=150, )

tel = Label(fenetre6, text="Téléphone", bg="#ffffff", fg="#000000").place(x=500, y=180)

telchamp = Entry(fenetre6, bg="white", width=25, font=('Calistoga', 12))
telchamp.place(x=500, y=210, )

# en tete
aff.heading(1, text="ID")
aff.heading(2, text="Nom")
aff.heading(3, text="Prénom")
aff.heading(4, text="Télephone")
aff.heading(5, text="Type de produit")
aff.heading(6, text="Adresse")
# dimension des colonnes
aff.column(1, width=10)
aff.column(2, width=10)
aff.column(3, width=10)
aff.column(4, width=10)
aff.column(5, width=10)
aff.column(6, width=10)
# les buttons modification
pad = customtkinter.CTkButton(master=fenetre6, text="Ajouter", command=ajouter, text_font=('Calistoga', 15),text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#319BFE")
pad.place(x=150, y=250)
pad = customtkinter.CTkButton(master=fenetre6, text="Supprimer", text_font=('Calistoga', 15), command=supprimer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="red")
pad.place(x=300, y=250)
pad = customtkinter.CTkButton(master=fenetre6, text="Modifier", text_font=('Calistoga', 15), command=modifier,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#6d071a")
pad.place(x=450, y=250)
pad = customtkinter.CTkButton(master=fenetre6, text="Récupérer", text_font=('Calistoga', 15), command=recuperer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="green")
pad.place(x=600, y=250)


#recherche champ
padchamp= Entry(fenetre6,font=('Calistoga',10),width=20,bg="#ffffff")
padchamp.place(x=740,y=254)

# bouton recherher
rech=Button(master=fenetre6,text="Rechercher",command=recherche,width=10)
rech.place(x=900,y=250)


# suivante et precedente
pad = Button(master=fenetre6, text="<<Précedente", font=('Calistoga', 11), command=quit, fg="#000000",
             width=11, bg="#ffffff")
pad.place(x=700, y=580)

pad = Button(master=fenetre6, text="Suivante>>", font=('Calistoga', 11), command=quit, fg="#000000",
             width=10, bg="#ffffff")
pad.place(x=850, y=580)

aff.bind("<Double-Button>",callback)

# bar= ttk.Scrollbar(fenetre6,orient="vertical",command=aff.yview)
# bar.place(x=980,y=290,height=280)

fenetre6.mainloop()