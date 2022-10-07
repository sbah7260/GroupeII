

#page des  magasiniers pour admin


from subprocess import call
from tkinter import *
import pymysql as pymysql
from tkinter import ttk,Entry
import customtkinter as customtkinter
from tkinter import messagebox



def retour():
    fenetre5.destroy()
    call(["python","accadmin.py"])



fenetre5=Tk()
fenetre5.title("Modification des magasinier ")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")
fenetre5.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\22926756.ico')

#les fonctions

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select id,nom,prenom,date_arrivee,telephone,adresse,email from mag ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,prenom,adresse,telephone,date_arrivee,email) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,prenom,adresse,telephone,date_arrivee,email))

    con.close()



# def modifier():
#     id = idchamp.get()
#     nom = nomchamp.get()
#     prenom = prechamp.get()
#     date = datechamp.get()
#     adresse = adressechamp.get()
#     telephone = telchamp.get()
#
#
#     con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
#     cursor = con.cursor()
#     cursor.execute("update mag set nom='"+ nom +"',prenom='"+ prenom +"',date_arrivee='" +date+ "',telephone='" +telephone+ "',adresse='" +adresse+ "',email='" +email+ "' where telephone='" +telephone+ " '")
#     cursor.execute("commit")
#     idchamp.delete(0, "end")
#     nomchamp.delete(0, "end")
#     prechamp.delete(0, "end")
#     telchamp.delete(0, "end")
#     adressechamp.delete(0, "end")
#     datechamp.delete(0, "end")
#     afficher()
#
#     con.close()

def supprimer():
    if (idchamp.get() == " " ):
        messagebox.showinfo("Message d'erreur", "Inserer l'ID");
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute("delete from mag where id='" + idchamp.get() + "' ")
        cursor.execute("commit")

        idchamp.delete(0, "end")
        nomchamp.delete(0, "end")
        prechamp.delete(0, "end")
        telchamp.delete(0, "end")
        adressechamp.delete(0, "end")
        datechamp.delete(0, "end")
        afficher()
        con.close()
def recuperer():

    id = idchamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("select id,nom,prenom,date_arrivee,telephone,adresse,email from mag where id='" + idchamp.get() + "'")
    rows = cursor.fetchall()
    cursor.execute("commit")

    idchamp.delete(0, "end")
    for row in rows:
        idchamp.insert(0, row[0])
        nomchamp.insert(0, row[1])
        prechamp.insert(0, row[2])
        telchamp.insert(0, row[4])
        adressechamp.insert(0, row[5])
        datechamp.insert(0, row[3])
        emailchamp.insert(0, row[6])
        afficher()
        con.close()




texte=Label (fenetre5,text="Magasiniers",font=('Calistoga',25),bg="white")
texte.place(x=400,y='',)
ret = Button(fenetre5, text="<<Retour", font=('Calistoga', 15), bg="#d9d9d9",command=retour)
ret.place(x=5, y='', )



id=Label(fenetre5, text="ID",bg="#ffffff",fg="#000000").place(x=340, y=70)

idchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
idchamp.place(x=340,y=90,)

nom = Label(fenetre5, text="Nom",bg="#ffffff",fg="#000000").place(x=50, y=120)

nomchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
nomchamp.place(x=50,y=150,)

prenom = Label(fenetre5, text="Prénom",bg="#ffffff",fg="#000000").place(x=50, y=180)

prechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
prechamp.place(x=50,y=210,)

date = Label(fenetre5, text="Date arrivée",bg="#ffffff",fg="#000000").place(x=650, y=120)

datechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
datechamp.place(x=650,y=150,)

email = Label(fenetre5, text="Email",bg="#ffffff",fg="#000000").place(x=650, y=180)

emailchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
emailchamp.place(x=650,y=210,)
adresse = Label(fenetre5, text="Adresse",bg="#ffffff",fg="#000000").place(x=340, y=120)

adressechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
adressechamp.place(x=340,y=150,)

telephone = Label(fenetre5, text="Téléphone",bg="#ffffff",fg="#000000").place(x=340, y=180)

telchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12))
telchamp.place(x=340,y=210,)

#affichage resultat
aff= ttk.Treeview(fenetre5, columns=(1,2,3,4,5,6,7),height=10,show="headings")
aff.place(x='',y='290',width=1000,height=280)
#en tete
aff.heading(1,text="ID")
aff.heading(2,text="Nom")
aff.heading(3,text="Prénom")
aff.heading(4,text="Date arrivée")
aff.heading(5,text="Téléphone")
aff.heading(6,text="Adresse")
aff.heading(7,text="Email")
#dimension des colonnes
aff.column(1,width=10)
aff.column(2,width=10)
aff.column(3,width=10)
aff.column(4,width=10)
aff.column(5,width=10)
aff.column(6,width=10)
aff.column(7,width=10)
#les buton modification
# pad= customtkinter.CTkButton(master=fenetre5,text="Ajouter",text_font=('Calistoga',11),command=ajouter,
#                                       height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
# pad.place(x=150,y=250)
pad = customtkinter.CTkButton(master=fenetre5, text="Supprimer", text_font=('Calistoga', 15), command=supprimer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="red")
pad.place(x=300, y=250)
# pad = customtkinter.CTkButton(master=fenetre5, text="Modifier", text_font=('Calistoga', 15), command=modifier,text_color='white',
#                               height=20, width=100, border_width=1, corner_radius=3, fg_color="#6d071a")
# pad.place(x=450, y=250)
pad = customtkinter.CTkButton(master=fenetre5, text="Récupérer", text_font=('Calistoga', 15), command=recuperer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="green")
pad.place(x=450, y=250)



# #recherche champ
# padchamp= Entry(fenetre6,font=('Calistoga',10),width=20,bg="#ffffff")
# padchamp.place(x=740,y=254)
#
# # bouton recherher
# rech=Button(master=fenetre6,text="Rechercher",command=recherche,width=10)
# rech.place(x=900,y=250)

#suivante et precedente
pad=Button(master=fenetre5,text="<<Précedente",font=('Calistoga',11),command=quit,fg="#000000",
                                      width=11,bg="#ffffff")
pad.place(x=700,y=580)

pad=Button(master=fenetre5,text="Suivante>>",font=('Calistoga',11),command=quit,fg="#000000",
                                     width=10,bg="#ffffff")
pad.place(x=850,y=580)

# bar= ttk.Scrollbar(fenetre5,orient="vertical",command=aff.yview)
# bar.place(x=980,y=290,height=280)

afficher()

fenetre5.mainloop()