import numpy as np
sales = np.array([
    10000,
    12000,
    15000,
    9000,
    18000
])
products = np.array([
    "Milk",
    "Bread",
    "Sugar",
    "Juice",
    "Rice"
])
target=12000
print(products [sales>=target])
