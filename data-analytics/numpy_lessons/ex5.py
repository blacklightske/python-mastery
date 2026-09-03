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
print("average is",sales.mean())
print("diff with average ",sales-np.mean(sales))
diff=sales-np.mean(sales)
print('furthest from average',diff[diff.argmax()])
print('furthest below average',diff[diff.argmin()])
#this tells the owner the varance of sales in the das which are perfoming okay and which days are getting highest number of ssles or perfoming okay 