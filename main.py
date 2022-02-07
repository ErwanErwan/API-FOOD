
import requests
import json

url = "https://world.openfoodfacts.org/api/v0/product/3017620425035.json" 
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
    
code()
print("---------")
keyword()
print("---------")
allergen()
print("---------")
brand()
