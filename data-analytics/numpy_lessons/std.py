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
saes = np.array([
    [100, 200, 300, 400],  # Monday
    [150, 250, 350, 450],  # Tuesday
    [120, 220, 320, 420]   # Wednesday
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
print("25th percentile",np.percentile(sales,25))
print("50th percentile",np.percentile(sales,50))
print("75th percentile",np.percentile(sales,75))
print("hello",saes.sum(axis=0))