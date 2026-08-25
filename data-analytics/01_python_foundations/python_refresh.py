sales = [12000, 15000, 9000, 18000, 25000]

diff1 = max(sales) - min(sales)
sales.insert(3, 11000)
sales[3] = 2005

print("sales of the day :", sales[0])
print("sales of the day :", sales[4])
print(sales)

print("Number of sales records:", len(sales))
print("Total sales:", sum(sales))
print("Average sales:", sum(sales) / len(sales))
print("Highest sales:", max(sales))
print("Lowest sales:", min(sales))
print("diff:", diff1)
