import numpy as np

sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [120, 220, 320, 420]
])

#print(sales.ndim,sales.shape,sales.size,sales)
#ex b
print(sales[0:])




mon_sales=sum(sales[0,:])
print(mon_sales)
sugar_sales=sum(sales[:,2])
print(sugar_sales)
juice_sales=sum(sales[:,3])
print(juice_sales)