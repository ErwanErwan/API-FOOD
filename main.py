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
