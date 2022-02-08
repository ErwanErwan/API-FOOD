import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
 
root = tk.Tk()
img_url = "https://fr.openfoodfacts.org/images/products/762/221/044/9283/front_fr.437.200.jpg"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
