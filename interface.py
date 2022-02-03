import time
import tkinter
from time import sleep


fenetre = tkinter.Tk()
fenetre.title("FoodChecker")
fenetre.wm_minsize(500,700)
fenetre.configure(bg="Green")

page_principale = tkinter.Frame(fenetre)
phrase = tkinter.Label(page_principale,text='Quel aliment recherchez vous ? :').pack(side="left")
recherche = tkinter.Entry(page_principale)
recherche.pack(side="left", fill="both", expand=1)
recherche.focus_set()
recherche_boutton = tkinter.Button(page_principale, text='Rechercher')
recherche_boutton.pack(side="right")
page_principale.pack(side="top")

product = []


def find():

    r = recherche.get()
    for i in range(len(product)):
        if product[i] == r:
            return product[i]
        else:
            i +=1
    else:
        print("nous n'avons pas trouvé")


recherche_boutton.config(command=find)
fenetre.mainloop()
