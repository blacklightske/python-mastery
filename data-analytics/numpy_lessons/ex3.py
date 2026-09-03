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
print("day with highest sales",days[(sales.argmax())])
print("day with lowest sales",days[sales.argmin()])
print("highest sales ",sales.argmax())
print("actual sales on the worst day ",sales.argmin())
diff= sales.max()-sales.min()
print("sales difference between worst and best day ",diff)

#this data tells the shop keeperthat friday had the hifghest sales more than monday with a difference of 12000 