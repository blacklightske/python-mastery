import numpy as np

products = np.array(["Milk", "Bread", "Sugar", "Juice"])
prices = np.array([100, 60, 80, 150])
quantity = np.array([20, 30, 10, 5])

revenue=prices*quantity
print(revenue)

#ex 2
print(products[quantity>10])
#ex3
new_prices=prices*11.5
print(new_prices)

#milk
#juice
#milk bread
#they increasse b 15%