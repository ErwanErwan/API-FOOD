import requests
import json

barre=int(input("Code Barre : "))

url = "https://world.openfoodfacts.org/api/v0/product/"+str(barre)+".json" 
response = requests.get(url)
data = json.loads(response.text)
#print(data)

prod = data["product"]["id"]

def code():
    print(data["product"]["id"])


def keyword():
    for i in range(len(data["product"]["_keywords"])):
        print(data["product"]["_keywords"][i])


def allergen():
    print(data["product"]["allergens_from_ingredients"])

def brand():
    print(data["product"]["brands"])

def nutriscore():
    print(data["product"]["nutrition_grade_fr"])
    
code()
print("---------")
keyword()
print("---------")
allergen()
print("---------")
brand()
print("---------")
nutriscore()


def nom():
    print(data["product"]["product_name_fr"])
