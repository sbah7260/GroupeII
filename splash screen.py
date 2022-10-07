import time
from subprocess import call
from tkinter import *


root = Tk()
root.title("Splash Screen")
root.geometry("600x400")
root.resizable(FALSE, FALSE)
root.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\BIG STOCK1.ico')
#root.overrideredirect(True)
photo = PhotoImage(file=r"BIG STOCK1.png")

l1 = Label(root, image=photo, border=0, relief=SUNKEN).place(x=220, y=100)

r = Label(root, text="Chargement ...", font=('Italic', 15))
r.place(x=430, y=360)


def admin():
    root.destroy()
    call(["python", "conexion.py"])


root.after(1500, admin)


"""l=Button(image = photo , bg ="#d9d9d9")
l.place(x=420, y=190)"""

"""r= Label(root, text="Chargement ...", font =('Italic',20) )
r.place(x=410, y=430)"""

"""for i in range(5):
    l1=Label(root, image= photo, border=0, relief=SUNKEN).place(x=180, y=190)
    l2 = Label(root, image=photo, border=0, relief=SUNKEN).place(x=200, y=190)
    l3 = Label(root, image=photo, border=0, relief=SUNKEN).place(x=220, y=190)
    l4 = Label(root, image=photo, border=0, relief=SUNKEN).place(x=240, y=190)
    root.update_idletasks()
    time.sleep(0.5)"""

root.mainloop()
