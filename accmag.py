

# page acceuil mag
from subprocess import call
from tkinter import *
from tkinter import ttk
import pymysql as pymysql
import customtkinter as customtkinter
from PIL import Image, ImageTk


# import mysql.connector
# from tkinter import mess



fenetre3 = Tk()
fenetre3.title("page d'acceil Admin")
fenetre3.geometry("1000x620")
fenetre3.resizable(False, False)
fenetre3.configure(bg="white")
fenetre3.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\img.ico')
fenetre3.wm_attributes('-transparentcolor', 'red')

def produit():
    fenetre3.destroy()
    call(["python", "prodmag.py"])


def retour():
    fenetre3.destroy()
    call(["python", "accmag.py"])


def prod():
    fenetre3.destroy()
    call(["python", "prodmag.py"])


def four():
    fenetre3.destroy()
    call(["python", "fourmag.py"])


def vente():
    fenetre3.destroy()
    call(["python", "ventes.py"])


def deconnexion():
    fenetre3.destroy()
    call(["python", "conexion.py"])


def total3():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from produit")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r
def total4():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from four")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r

def total5():
    conn = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = conn.cursor()
    cursor.execute("select count(id) from mag")
    records = cursor.fetchall()
    for row in records:
        r=row[0]
        r=str(r)
        return r

# corps
fram = Frame(fenetre3, bg='#FFFFFF', width='1000', height='250')
fram.place(x='', y='')

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))
x = Label(fram, image=photo)
x.place(x='0', y='')

# Label(master=fram, text="Accueil",font=('Calistoga', 30),
#                                  fg='#319BFE').place(x='10', y='150')
# bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,
#                                  fg_color='#319BFE',corner_radius=15, border_width=1, command=prod)
# bouton.place(x='180', y='170')
# bouton = customtkinter.CTkButton(master=fram, text="Vente", text_font=('Calistoga', 20), width=170, height=20,
#                                  fg_color='#319BFE',corner_radius=15, border_width=1, command=vente)
# bouton.place(x='360', y='170')
# bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,
#                                  fg_color='#319BFE',corner_radius=15, border_width=1, command=four)
# bouton.place(x='570', y='170')
# bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,
#                                  fg_color='#319BFE',corner_radius=15, border_width=1, command=deconnexion)
# bouton.place(x='800', y='170')

acc = Label(fram, text="Accueil", font=('Italic', 25))
acc.place(x="20", y="165")
bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE', corner_radius=15, border_width=1,bg_color='red', command=prod)
bouton.place(x='180', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Vente", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE', corner_radius=15, border_width=1, bg_color='red', command=vente)
bouton.place(x='380', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE', corner_radius=15, border_width=1, bg_color='red', command=four)
bouton.place(x='570', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE', corner_radius=15, bg_color='red', borderwidth=0, command=deconnexion)
bouton.place(x='800', y='170')


# recherche
logo = Label(fram, text="Bienvenue Magasinier!!!", font=('Italic', 15))
logo.place(x="780", y="10")
# logo
logo = Label(fram, text=" BigStock", font=('Italic', 50))
logo.place(x="10", y="10")

fram0 = Frame(fenetre3, width='1000', height='370')
fram0.place(x='', y='250')

# logo=PhotoImage(file=r"BIG STOCK1.png")
# img=Button( image=logo).place(x=10,y=20)
pro = Label(fram0,text="Total Produits  \n" + total3(), bg="#319BFE",fg="white", width="15", height="4",font=('', 20,))
pro.place(x="150", y="80")
pro1 = Label(fram0,text="Total Fournisseur  \n" + total4(), bg="#319BFE",fg="white", width="15", height="4",font=('', 20,))
pro1.place(x="550", y="80")
# pro2 = Label(fram0,text="Total Magasinier  \n" + total5(), bg="#319BFE",fg="white", width="15", height="4",font=('', 20,))
# pro2.place(x="700", y="80")

# copyrith

preven = Label(fenetre3, text="Copyright @ 0101 par Groupe 2/ODC", font=("Arial", 10))
preven.place(x="350", y="600")


fenetre3.mainloop()
