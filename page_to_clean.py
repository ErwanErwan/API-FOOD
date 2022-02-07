import requests
import json
import tkinter

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

barre = 737628064502
url = "https://world.openfoodfacts.org/api/v0/product/" + str(barre) + ".json"
response = requests.get(url)
data = json.loads(response.text)
prod = data["product"]["id"]


def code():
    return data["product"]["id"]


def nom():
    return data["product"]["product_name"]


def keyword():
    for i in range(len(data["product"]["_keywords"])):
        print(data["product"]["_keywords"][i])


def allergen():
    return data["product"]["allergens_from_ingredients"]


def brand():
    return data["product"]["brands"]


def nutriscore():
    return data["product"]["nutrition_grade_fr"]


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
                  text="Nom :"+ (str(nom()))).pack()
    tkinter.Label(fenetre_produit,
                  text="Allegerne(s) : " + str(allergen())).pack()
    tkinter.Label(fenetre_produit,
                  text="Marque : " + str(brand())).pack()
    tkinter.Label(fenetre_produit,
                  text="Nutriscore : " + str(nutriscore()).upper()).pack()


def add_produit(produit):
    return product.append(produit)


def recherche_produit():
    r = barre_search.get()
    for i in range(len(product)):
        if product[i] == r:
            return fenetre_produit(product[i])
        else:
            i += 1
    else:
        print("nous n'avons pas trouvé")

code()
print("---------")
keyword()
print("---------")
allergen()
print("---------")
brand()
print("---------")
nutriscore()

add_produit(barre_search)
recherche_boutton.config(command=recherche_produit)
base.mainloop()
