import tkinter

base = tkinter.Tk()
base.title("FoodChecker")
base.geometry("500x700")
base.configure(bg="Grey")

page_principale = tkinter.Frame(base)
tkinter.Label(page_principale, text='Quel aliment recherchez vous ? :').pack(side="left")
recherche = tkinter.Entry(page_principale)
recherche.pack(side="left", fill="both", expand=1)
recherche.focus_set()
recherche_boutton = tkinter.Button(page_principale, text='Rechercher')
recherche_boutton.pack(side="right")
page_principale.pack(side="top")

product = ["xiao"]


def fenetre_produit(nom_produit):
    """
    :param nom_produit: le nom du produit dont on doit créer la fentre
    :return : une nouvelle fenetre avec des informations
    """

    fenetre_produit = tkinter.Toplevel(base)
    fenetre_produit.title(nom_produit)

    fenetre_produit.geometry("500x300")

    # tkinter.Label(fenetre_produit,
    #               image= "xiao_portrait.png")
    tkinter.Label(fenetre_produit,
                  text="Nom : " + nom_produit).pack()
    tkinter.Label(fenetre_produit,
                  text="Sucre : " + str(1) + " gramme").pack()


# label_base_fenetre = tkinter.Label(base,
#                     text="Fenetre de base")

# label_base_fenetre.pack(pady=10)

# boutton_t = tkinter.Button(base, text="test",command=fenetre_produit)
# boutton_t.pack(pady=10)


def recherche_produit():
    r = recherche.get()
    for i in range(len(product)):
        if product[i] == r:
            return fenetre_produit(product[i])
        else:
            i += 1
    else:
        print("nous n'avons pas trouvé")


recherche_boutton.config(command=recherche_produit)
base.mainloop()