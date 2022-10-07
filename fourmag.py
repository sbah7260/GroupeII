
#page fournisseur magasinier et admin


from subprocess import call
from tkinter import *
from tkinter import Entry
import customtkinter as customtkinter
from tkinter import ttk
import pymysql as pymysql
from tkinter import messagebox


fenetre5=Tk()
fenetre5.title("Fourniseur ")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")

def retour():
    fenetre5.destroy()
    call(["python","accmag.py"])

#affichage resultat
aff= ttk.Treeview(fenetre5, columns=(1,2,3,4,5,6),height=10,show="headings")
aff.place(x='',y='290',width=1000,height=280)

#nouveau fonction

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select * from four ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,prenom,tel,typro,adresse) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,prenom,tel,typro,adresse))

    con.close()

afficher()

#les fonctions


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
        messagebox.showinfo("Message d'erreur", "Tout les champs sont réquis")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute("insert into four values('" + id + "','" + nom + "','" + prenom + "','" + tel + "','" + typro + "','" + adresse + "') ")
        cursor.execute("commit")

    idchamp.delete(0,"end")
    nomchamp.delete(0,"end")
    prechamp.delete(0,"end")
    telchamp.delete(0,"end")
    adreschamp.delete(0,"end")
    typrochamp.delete(0,"end")
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
    adresse=adreschamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("update four set id='"+id +"',nom='" + nom + "',prenom='" + prenom + "',tel='" + tel + "',typro='" + typro + "',adresse='" + adresse + "' where id='" + id + " '")
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




texte=Label (fenetre5,text="Fournisseurs",font=('Calistoga',25),bg="white")
texte.place(x=400,y='',)
ret = Button(fenetre5, text="<<Retour", font=('Calistoga', 15), bg="#d9d9d9",command=retour)
ret.place(x=5, y='', )


id = Label(fenetre5, text="ID",bg="#ffffff",fg="#000000").place(x=50, y=80)

idchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
idchamp.place(x=50,y=100,)

nom = Label(fenetre5, text="Nom",bg="#ffffff",fg="#000000").place(x=50, y=130)

nomchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
nomchamp.place(x=50,y=150,)

prenom = Label(fenetre5, text="Prénom",bg="#ffffff",fg="#000000").place(x=50, y=180)

prechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
prechamp.place(x=50,y=210,)

typro = Label(fenetre5, text="Type de produit",bg="#ffffff",fg="#000000").place(x=340, y=80)

typrochamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
typrochamp.place(x=340,y=100,)

adresse = Label(fenetre5, text="Adresse",bg="#ffffff",fg="#000000").place(x=340, y=130)

adreschamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
adreschamp.place(x=340,y=150,)

tel = Label(fenetre5, text="Téléphone",bg="#ffffff",fg="#000000").place(x=340, y=180)

telchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
telchamp.place(x=340,y=210,)



#en tete
aff.heading(1,text="ID")
aff.heading(2,text="Nom")
aff.heading(3,text="Prénom")
aff.heading(4,text="Télephone")
aff.heading(5,text="Type de produit")
aff.heading(6,text="Adresse")
#dimension des colonnes
aff.column(1,width=10)
aff.column(2,width=10)
aff.column(3,width=10)
aff.column(4,width=10)
aff.column(5,width=10)
aff.column(6,width=10)
#les buton modification
pad = customtkinter.CTkButton(master=fenetre5, text="Ajouter", command=ajouter, text_font=('Calistoga', 15),text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#319BFE")
pad.place(x=150, y=250)
pad = customtkinter.CTkButton(master=fenetre5, text="Supprimer", text_font=('Calistoga', 15), command=supprimer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="red")
pad.place(x=300, y=250)
pad = customtkinter.CTkButton(master=fenetre5, text="Modifier", text_font=('Calistoga', 15), command=modifier,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#6d071a")
pad.place(x=450, y=250)
pad = customtkinter.CTkButton(master=fenetre5, text="Récupérer", text_font=('Calistoga', 15), command=recuperer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="green")
pad.place(x=600, y=250)

#suivante et precedente
# pad=Button(master=fenetre5,text="<<Précedente",font=('Calistoga',11),command=quit,fg="#000000",
#                                       width=11,bg="#ffffff")
# pad.place(x=700,y=580)
#
# pad=Button(master=fenetre5,text="Suivante>>",font=('Calistoga',11),command=quit,fg="#000000",
#                                      width=10,bg="#ffffff")
# pad.place(x=850,y=580)

bar= ttk.Scrollbar(fenetre5,orient="vertical",command=aff.yview)
bar.place(x=980,y=290,height=280)


#recherche champ
padchamp= Entry(fenetre5,font=('Calistoga',10),width=20,bg="#ffffff")
padchamp.place(x=740,y=254)

# bouton recherher
rech=Button(master=fenetre5,text="Rechercher",command=recherche,width=10)
rech.place(x=900,y=250)

# def admin():
#     fenetre5.destroy()
#     # call(["python","conexion.py"])
#     import conexion
#
#
# fenetre5.after(1500, admin)


fenetre5.mainloop()