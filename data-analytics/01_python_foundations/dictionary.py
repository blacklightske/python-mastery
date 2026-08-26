product ={
    "name": "milk",
    "price": 100,
    "quantity_sold": 25
}

#product name print
print(product["name"])
print(product["price"])
print(product["quantity_sold"])
product["price"]=120
print(product["price"])
product["category"]=("dairy")
print(product)
print(product.values())

#excercise 3
revenue=product["price"]*product["quantity_sold"]
print("revenue for this month is:",revenue)