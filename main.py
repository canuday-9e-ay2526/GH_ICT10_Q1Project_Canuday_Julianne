# SKU and Reciept Generator
from pyscript import display, document

  

def create_order(e):
    #get all elements
    prod1 = document.getElementById("Cat")
    prod2 = document.getElementById("Bird")
    prod3 = document.getElementById("Jellyfish")
    prod4 = document.getElementById("AnimalStickers")

    #Add all product values
    subtotal = (
        (float(prod1.value) * prod1.checked) + (float(prod2.value) * prod2.checked) + (float(prod3.value) * prod3.checked) +
        (float(prod4.value) * prod4.checked))
    Tax=1.12
    Total=float(subtotal)*float(Tax)

    #Display output
    document.getElementById('output1').innerHTML=f'Subtotal:{subtotal}<br>Tax:{Tax}<br>Total:{Total}'

def generate_sku(e):
    #Get all element values
    Category = document.getElementById("category").value
    Product = document.getElementById("product").value
    Quantity = int(document.getElementById("quantity").value)

    #abbreviate product name
    Product_skuval = Product[:3]

    #set quantity number to a 3 digit number if lower than 100
    quantity_skuval = f'{Quantity:03d}'

 
    #Display output
    document.getElementById('output2').innerHTML=f'{Category}-{Product_skuval.upper()}-{quantity_skuval}'



