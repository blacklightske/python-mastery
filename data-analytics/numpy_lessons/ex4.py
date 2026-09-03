import numpy as np
sales = np.array([8000, 12000, 15000, 10000, 20000, 18000, 9000])

days = np.array([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])

print("indexes of lowest to highest ",sales.argsort())
print("days from lowest to largest ",days[sales.argsort()])
print("days from highest to lowest",days[sales.argsort()[::-1]])
print("sales amount from highest to lowest ",sales[sales.argsort()[::-1]])
#the difference between the argmax and argsort is that argmax returns the index of the hisest value while argsort returns the index in array arranged from smallest to largest by default