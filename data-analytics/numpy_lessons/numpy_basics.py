import numpy as np 
sales=np.array([12000,15000,9000,18000,25000])

print(sales)
print("the first value is :",sales[0])
print("the last value is :",sales[4])
print("the total is ",sales.sum())
print("the average is :",sales.mean())
print("the highet value is:",sales.max())
print("the lowest value is:",sales.min())
projected_sales=sales*1.1
print("increased sales is:",projected_sales)