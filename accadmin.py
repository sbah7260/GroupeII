#page acceuil admin
from subprocess import call
from tkinter import *
#from tkinter import ttk
import pymysql as pymysql
import customtkinter as customtkinter
from PIL import Image, ImageTk


def prodadmin():
    fenetre2.destroy()
    call(["python", "prodadmin.py"])


def fournisseur():
    fenetre2.destroy()
    call(["python", "fournisseur.py"])

def magasinier():
    fenetre2.destroy()
    call(["python", "magasinier.py"])

def deconnexion():
    fenetre2.destroy()
    call(["python", "conexion.py"])
#afficher le total apprenants sur le dashboard

def total():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from produit")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r
def total1():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from four")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r

def total2():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from mag")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r

fenetre2 = Tk()
fenetre2.title("page d'acceil Admin")
fenetre2.geometry("1000x620")
fenetre2.resizable(False, False)
fenetre2.configure(bg="white")
fenetre2.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\img.ico')
fenetre2.wm_attributes('-transparentcolor', 'red')

# can = Canvas(fenetre2, width=1000, height=275, bg="#0ea598")
# img = PhotoImage(file="C:\\Users\\lenovo\\PycharmProjects\\pythonProject1\\BigStock\\stock.gif")
# can.create_image(1000,275, anchor=NW, image=img)
# can.place(x="",y="")
# corps
fram = Frame(fenetre2, bg='#FFFFFF', width='1000', height='250')
fram.place(x='', y='')

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))
x = Label(fram, image=photo)
x.place(x='', y='')
acc = Label(fram, text="Accueil", font=('Italic', 25))
acc.place(x="20", y="165")
# bouton = customtkinter.CTkButton(master=fram, text="Accueil", text_font=('Calistoga', 20), width=100, height=20,
#                                  fg_color='#319BFE',corner_radius=15, border_width=1, bg_color='red', cursor='hand2')
# bouton.place(x='10', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,text_color='white',
                                 fg_color='#319BFE', corner_radius=15, border_width=1,bg_color='red', command=prodadmin)
bouton.place(x='180', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Magasinier", text_font=('Calistoga', 20), width=100, height=20,text_color='white',
                                 fg_color='#319BFE', corner_radius=15, border_width=1, bg_color='red', command=magasinier)
bouton.place(x='360', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,text_color='white',
                                 fg_color='#319BFE', corner_radius=15, border_width=1, bg_color='red', command=fournisseur)
bouton.place(x='570', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,text_color='white',
                                 fg_color='#319BFE', corner_radius=15, bg_color='red', borderwidth=0, command=deconnexion)
bouton.place(x='800', y='170')
# recherche
logo = Label(fram, text="Bienvenue Administrateur!!!", font=('Italic', 15))
logo.place(x="750", y="10")
# logo
logo = Label(fram, text=" BigStock", font=('Italic', 50))
logo.place(x="10", y="10")
#insertion de la frame
fram = Frame(fenetre2, width='1000', height='370')
fram.place(x='', y='250')

# logo=PhotoImage(file=r"BIG STOCK1.png")
# img=Button( image=logo).place(x=10,y=20)

# logo=PhotoImage(file=r"BIG STOCK1.png")
# img=Button( image=logo).place(x=10,y=20)
prod = Label(fram,text="Total Produits  \n" + total(), bg="#90ee90",fg="white", width="13", height="4",font=('', 20,))
prod.place(x="30", y="80")
prod1 = Label(fram,text="Total Fournisseur  \n" + total1(), bg="#F7FF3C",fg="white", width="14", height="4",font=('', 20,))
prod1.place(x="355", y="80")
prod2 = Label(fram,text="Total Magasinier  \n" + total2(), bg="#6d071a",fg="white", width="14", height="4",font=('', 20,))
prod2.place(x="700", y="80")
#lblTa = Label(fen1,text=""+total(), font=("Berlin Sans FB", 25), bg="#FF5F04")
#lblTa.place(x=930,y=310, width=400,height=170


# copyrith
preven = Label(fenetre2, text="Copyright @ 0101 par Groupe 2/ODC", font=("Arial", 10))
preven.place(x="370", y="600")

fenetre2.mainloop()

