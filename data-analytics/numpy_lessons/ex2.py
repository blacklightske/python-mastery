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
print("sum is:",sales.sum())
#the total weekly sales are 92000
print("mean is:",sales.mean())
#the average daily sals are13142.8571
print("median is:",np.median(sales))
#the media. is
print("min is:",sales.min())
#the weakest sales value is 8000
print("max is:",np.max(sales))
#the strongest sales value is 20000
#the average bing higher than the median it suggests that there are some days the 
# sales spikes more than others hence the diference observed 
average=sales.mean()
print('avrage is ,',sales>average)
print((sales>average).sum())
print(sales[sales>average])
#days of the week 