import requests
import json

url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"
response = requests.get(url)
data = json.loads(response.text)
# print(data)

prod = data["product"]["id"]


def produit(info):
    inf = data[str(info)]
    print(inf)


def rech(p):
    print(data["product"]["_keywords"])


# produit("code")
# print(prod)
rech("0")
# produit("product")