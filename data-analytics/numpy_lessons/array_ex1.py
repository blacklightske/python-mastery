import numpy as np

sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [120, 220, 320, 420]
])

print("exercise a ",sales.ndim,sales.shape,sales.size,sales)
#ex b
print("monday milk sales",sales[0,0])
print("tuesday sugar sales",sales[1,2])
print("wednesday juice sales",sales[2,3])



#exedrcise c
mon_sales=sales[0,:].sum(). #alternative ue of sum this is for numpy 
print("mon sales are ",mon_sales)
sugar_sales=sum(sales[:,2])
print("sugar sales are ",sugar_sales)
juice_sales=sum(sales[:,3])
print("juice sales are ",juice_sales)


# ex d
#adress of the item in row 3 column 1  ..this are indexes 
#ndim tells us the dimention of the array if its 3d or 2d (like number if rows array has)
#size tells us the total number of items in the array