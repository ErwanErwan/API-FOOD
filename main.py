import json
import tkinter
from PIL import ImageTk, Image
import requests
from io import BytesIO

global product
product = []

"""
 ________   _______       _________   ______  ______        ______      ______    _________  
|_   __  | |_   __ \     |  _   _  | |_   _ `|_   _ `.    .' ___  |   .' ____ \  |  _   _  | 
  | |_ \_|   | |__) |    |_/ | | \_|   | | `. \| | `. \  / .'   \_|   | (___ \_| |_/ | | \_| 
  |  _| _    |  __ /         | |       | |  | || |  | |  | |   ____    _.____`.      | |     
 _| |__/ |  _| |  \ \_      _| |_     _| |_.' _| |_.' /  \ `.___]  |  | \____) |    _| |_    
|________| |____| |___|    |_____|   |______.|______.'    `._____.'    \______.'   |_____|                                                                                           
"""                                                                            
class Product:

    def __init__(self, code_barre):
        self.cb = code_barre
        self.url = self.get_url()
        self.name = str(self.nom())
        self.kw = str(self.keyword())
        self.b = str(self.brand())
        self.ns = str(self.nutriscore()).upper()
        self.sugar = str(self.sucre())
        global product
        product.append(self)

    def get_url(self):
        """
        :return: renvoie les données associés au code barre
        """
        url = "https://world.openfoodfacts.org/api/v0/product/" + str(self.cb) + ".json"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def code(self):
        """
        :return: renvoie
        """
        return self.url["product"]["id"]

    def nom(self):
        """
        :return: renvoie le nom du produit
        """
        return self.url["product"]["product_name"]

    def keyword(self):
        """
        :return: renvoie les mots clefs associés au produit
        """
        mot = ""
        g = 0
        for i in range(len(self.url["product"]["_keywords"])):
            if g > 20:
                mot = mot + " \n " + str(self.url["product"]["_keywords"][i])
                g = -20
            else:
                mot = mot + " " + str(self.url["product"]["_keywords"][i])
                g += len(mot.split())
        return str(mot)

    def brand(self):
        """
        :return: renvoie la marque du produit
        """
        return self.url["product"]["brands"]

    def nutriscore(self):
        """
        :return: renvoie le nutriscore
        """
        return self.url["product"]["nutrition_grade_fr"]

    def sucre(self):
        """
        :return: renvoie le nombre de gramme de sucre pour 100g
        """
        return self.url["product"]["nutriments"]["sugars_100g"]

    def image(self):
        img_url = self.url["product"]["image_front_small_url"]
        response = requests.get(img_url)
        img_data = response.content
        return img_data

    def fenetre_produit(self):
        """
        :return : une nouvelle fenetre avec des informations
        """
        fenetre_produit = tkinter.Toplevel()
        fenetre_produit.title(self.name)
        base.iconbitmap("openfoodfacts-logo.ico")
        fenetre_produit.geometry("335x375")
        fenetre_produit.minsize(width=335, height=365)
        fenetre_produit.maxsize(width=335, height=365)
        if self.ns == "A":
            fenetre_produit.configure(bg="#038141")
        elif self.ns == "B":
            fenetre_produit.configure(bg="#85bb2f")
        elif self.ns == "C":
            fenetre_produit.configure(bg="#fecb02")
        elif self.ns == "D":
            fenetre_produit.configure(bg="#ee8100")
        elif self.ns == "E":
            fenetre_produit.configure(bg="#e63e11")
        else:
            fenetre_produit.configure(bg="Grey")
        """img_url = self.url["product"]["image_front_small_url"]
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
       """
        img = ImageTk.PhotoImage(Image.open(BytesIO(self.image())))
        tkinter.Label(master=fenetre_produit,
                      image=img, background="#ffffff").pack(side="top", anchor="n", expand="no", padx=1.0)
        tkinter.Label(fenetre_produit,
                      text="Mot(s)-Clef(s) : " + self.kw, background="#ffffff").pack(anchor="n", side="bottom",
                                                                                     fill="both")
        tkinter.Label(fenetre_produit,
                      text="Sucre pour 100g : " + self.sugar, background="#ffffff").pack(anchor="n", side="bottom",
                                                                                         fill="x")
        tkinter.Label(fenetre_produit,
                      text="Nutriscore : " + self.ns, background="#ffffff").pack(anchor="n", side="bottom", fill="x")
        tkinter.Label(fenetre_produit,
                      text="Marque : " + self.b, background="#ffffff").pack(anchor="n", side="bottom", fill="x")
        tkinter.Label(fenetre_produit,
                      text="Nom : " + self.name, background="#ffffff").pack(anchor="n", side="bottom", fill="x")

        fenetre_produit.mainloop()


#product.append(Product("3229820794624"))
#  product = [Product("3229820794624"), Product("3033710073467")]  # Liste des produits

# Fenetre initiale
base = tkinter.Tk()
base.title("FoodChecker")
base.geometry()
base.iconbitmap("openfoodfacts-logo.ico")
page_principale = tkinter.Frame(base)
# Code de la barre de recherche
tkinter.Label(page_principale, text='Quel aliment recherchez vous ? :').pack(side="left")
barre_search = tkinter.Entry(page_principale)
barre_search.pack(side="left", expand=1)
barre_search.focus_set()
# Code du boutton recherche
recherche_boutton = tkinter.Button(page_principale, text='Rechercher')
recherche_boutton.pack(side="left")
page_principale.pack(side="top")

produit_ex1 = tkinter.Button(page_principale, fg='Black', text="Coca Cola - 0,33 cl",
                             command=Product(5449000000996).fenetre_produit)
produit_ex1.config(width=30, height=2)
produit_ex2 = tkinter.Button(page_principale, fg='Black', text="Prince Chocolat - LU - 300 g",
                             command=Product(7622210449283).fenetre_produit)
produit_ex2.config(width=30, height=2)
produit_ex3 = tkinter.Button(page_principale, fg='Black', text="Dolce pizza prosciutto - Sodebo - 400 g",
                             command=Product(3242272346050).fenetre_produit)
produit_ex3.config(width=30, height=2)
produit_ex1.pack()
produit_ex2.pack()
produit_ex3.pack()


barre = barre_search


def recherche_produit():
    r = barre_search.get()
    product.append(r)
    for i in range(len(product)):
        if product[i] == r:
            return Product(product[i]).fenetre_produit()
        else:
            i += 1
    else:
        print("nous n'avons pas trouvé")


recherche_boutton.config(command=recherche_produit)
base.mainloop()
