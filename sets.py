list_example = [1, 1, 3, 3, 2, 5]
print(list_example)

var = set(list_example)
print(var)
# print(var[2])

if 3 in var:
    print("True")
else:
    print("False")

var1 = set([])
var1.add(14)
var1.add(16)
var1.add(23)
var1.add(14)
print(var1)

var1.remove(14)
print(var1)

var1.discard(14)
print(var1)

# Set Operations
set1 = {3, 4, 6, 9, 12, 18}
set2 = {3, "a", 18, "c", "y"}

# Union
print(set1.union(set2))
print(set1|set2)

# Intersection
print(set1.intersection(set2))
print(set1&set2)

# Difference
print(set1.difference(set2))
print(set1 - set2)

# Symmetric Difference
print(set1.symmetric_difference(set2))
print(set1 ^ set2)