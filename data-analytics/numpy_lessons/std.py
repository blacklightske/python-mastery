import numpy as np

sales = np.array([
    8000,
    12000,
    15000,
    10000,
    20000,
    18000,
    9000
])

days = np.array([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])
print("standard deviation as observed is ",np.std(sales))