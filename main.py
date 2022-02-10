import json
import tkinter
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO


def get_url(code_barre):
    url = "https://world.openfoodfacts.org/api/v0/product/" + str(code_barre) + ".json"
    response = requests.get(url)
    global product
    product.append(code_barre)
    data = json.loads(response.text)
    return data


# prod = data["product"]["id"]

product = ["xiao", "737628064502"]
base = tkinter.Tk()
base.title("FoodChecker")
base.geometry("500x700")
base.configure(bg="Grey")

page_principale = tkinter.Frame(base)
tkinter.Label(page_principale, text='Quel aliment recherchez vous ? :').pack(side="left")
barre_search = tkinter.Entry(page_principale)
barre_search.pack(side="left", fill="both", expand=1)
barre_search.focus_set()
recherche_boutton = tkinter.Button(page_principale, text='Rechercher')
recherche_boutton.pack(side="right")
page_principale.pack(side="top")

barre = barre_search


def image(code_barre):
    img_url = get_url(code_barre)
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    return img


def code(barre):
    return get_url(barre)["product"]["id"]


def nom(barre):
    return get_url(barre)["product"]["product_name"]


def keyword(barre):
    mot = ""
    for i in range(len(get_url(barre)["product"]["_keywords"])):
        mot = mot + " " + str(get_url(barre)["product"]["_keywords"][i])
    return str(mot)


def brand(barre):
    return get_url(barre)["product"]["brands"]


def nutriscore(barre):
    return get_url(barre)["product"]["nutrition_grade_fr"]


def sucre(barre):
    return get_url(barre)["product"]["nutriments"]["sugars_100g"]



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
                  text="Nom :" + (str(nom(nom_produit)))).pack()
    tkinter.Label(fenetre_produit,
                  text="Marque : " + str(brand(nom_produit))).pack()
    tkinter.Label(fenetre_produit,
                  text="Sucre pour 100g : " + str(sucre(nom_produit))).pack()
    tkinter.Label(fenetre_produit,
                  text="Nutriscore : " + str(nutriscore(nom_produit)).upper()).pack()
    tkinter.Label(fenetre_produit,
                  text="Mot-Celf(s) :" + (str(keyword(nom_produit)))).pack()
    tkinter.Label(fenetre_produit(),
                  image=image(nom_produit)).pack(side="bottom", fill="both", expand="yes")


#tkinter.Image(fenetre_produit,
    #           image(nom_produit)).pack()


#def image_creation(barre):
#    width = 300
#    height = 300
#    canva = tkinter.Canvas(base, width=width, height=height)
#    canva.create_image(width, height, image=imagev2())

width = 300
height = 300
img = image(737628064502)
#img2 = imagev2()
canvas = tkinter.Canvas(base, width=width, height=height, bg="#4065A4")
canvas.create_image(width/2, height/2, image=img)
canvas.pack(expand="YES")


def recherche_produit():
    r = barre_search.get()
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
