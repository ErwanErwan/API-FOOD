import json
import tkinter
from PIL import ImageTk, Image
import requests
from io import BytesIO


def get_url(code_barre):
    """
    :param code_barre: le code barre d'un produit
    :return: renvoie les données associés au code barre
    """
    url = "https://world.openfoodfacts.org/api/v0/product/" + str(code_barre) + ".json"
    response = requests.get(url)
    global product
    product.append(code_barre)
    data = json.loads(response.text)
    return data


product = ["3229820794624"]  # Liste des produits
# Fenetre initiale
base = tkinter.Tk()
base.title("FoodChecker")
base.geometry("500x35")
base.maxsize(500, 35)
base.minsize(500, 35)
base.configure(bg="Grey")
base.iconbitmap("openfoodfacts-logo.ico")
page_principale = tkinter.Frame(base)
# Code de la barre de recherche
tkinter.Label(page_principale, text='Quel aliment recherchez vous ? :').pack(side="left")
barre_search = tkinter.Entry(page_principale)
barre_search.pack(side="left", fill="both", expand=1)
barre_search.focus_set()
# Code du boutton recherche
recherche_boutton = tkinter.Button(page_principale, text='Rechercher')
recherche_boutton.pack(side="right")
page_principale.pack(side="top")
barre = barre_search


def code(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie l'identifiant du produit (son code barre...fonction inutile mais sert d'exemple et d'explication)
    """
    return get_url(barre)["product"]["id"]


def nom(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie le nom du produit
    """
    return get_url(barre)["product"]["product_name"]


def keyword(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie les mots clefs associés au produit
    """
    mot = ""
    for i in range(len(get_url(barre)["product"]["_keywords"])):
        mot = mot + " " + str(get_url(barre)["product"]["_keywords"][i])
    return str(mot)


def brand(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie la marque du produit
    """
    return get_url(barre)["product"]["brands"]


def nutriscore(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie le nutriscore
    """
    return get_url(barre)["product"]["nutrition_grade_fr"]


def sucre(barre):
    """
    :param barre: code barre d'un produit
    :return: renvoie le nombre de gramme de sucre pour 100g
    """
    return get_url(barre)["product"]["nutriments"]["sugars_100g"]


def fenetre_produit(nom_produit):
    """
    :param nom_produit: le nom du produit dont on doit créer la fentre
    :return : une nouvelle fenetre avec des informations
    """
    fenetre_produit = tkinter.Toplevel()
    fenetre_produit.title(str(nom(nom_produit)))
    fenetre_produit.geometry("600x350")
    fenetre_produit.configure(bg="Black")
    img_url = get_url(nom_produit)["product"]["image_front_small_url"]
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    tkinter.Label(fenetre_produit,
                  text="Nom :" + (str(nom(nom_produit)))).pack(anchor="nw")
    tkinter.Label(fenetre_produit,
                  text="Marque : " + str(brand(nom_produit))).pack(anchor="nw")
    tkinter.Label(fenetre_produit,
                  text="Sucre pour 100g : " + str(sucre(nom_produit))).pack(anchor="nw")
    tkinter.Label(fenetre_produit,
                  text="Nutriscore : " + str(nutriscore(nom_produit)).upper()).pack(anchor="nw")
    tkinter.Label(master=fenetre_produit,
                  image=img).pack(anchor="ne", side="top", expand="no", padx=1.0)
    tkinter.Label(fenetre_produit,
                  text="Mot-Celf(s) :" + (str(keyword(nom_produit)))).pack(anchor="nw")
    fenetre_produit.mainloop()


def recherche_produit():
    r = barre_search.get()
    for i in range(len(product)):
        if product[i] != r:
            i +=1
        elif i == len(product):
            product.append(r)
    for i in range(len(product)):
        if product[i] == r:
            return fenetre_produit(product[i])
        else:
            i += 1
    else:
        print("nous n'avons pas trouvé")


recherche_boutton.config(command=recherche_produit)
base.mainloop()
