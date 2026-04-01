import random
results = []
list_low = []
list_medium = []
list_high = []
for i in range (20):
    number = random.randint(1, 100)
    results.append(number)
print(results)
for j in results:
    if j <= 30:
        list_low.append(j)
    elif j >=31 and j <=69:
        list_medium.append(j)
    else:
        list_high.append(j)
print(list_low)
print(list_medium)
print(list_high)