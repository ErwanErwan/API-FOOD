import requests
import json
import interface

barre=int(input("Code Barre : "))

url = "https://world.openfoodfacts.org/api/v0/product/"+str(barre)+".json" 
response = requests.get(url)
data = json.loads(response.text)
#print(data)

prod = data["product"]["id"]

def nom():
    return data["product"]["product_name_fr"]

def code():
    return data["product"]["id"]


def keyword():
    mot=""
    for i in range(len(data["product"]["_keywords"])):
        mot=mot+" "+str(data["product"]["_keywords"][i])
    print(str(mot)) 


def allergen():
    return data["product"]["allergens_from_ingredients"]

def brand():
    return data["product"]["brands"]

def nutriscore():
    return data["product"]["nutrition_grade_fr"]

#########################

def allergen():
    if data["product"]["allergens_from_ingredients"]:
        return data["product"]["allergens_from_ingredients"]
    else:
        return "Ce produit ne présente pas d'allergies."
##############################################

def sucre():
    return data["product"]["nutriments"]["sugars_100g"]

#########################################

def image():
    img_url = data["product"]["image_front_small_url"]
    print(img_url)
    response= requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img.show()

    ############################## 
print(nom())
print("---------")
print(code())
print("---------")
print(keyword())
print("---------")
print(allergen())
print("---------")
print(brand())
print("---------")
print(nutriscore())


#########################

def image():
    return data["product"]["image_front_small_url"]
