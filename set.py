set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
print("Before: ")
print(set1)
print(len(set1))

# add function
set1.add(9)
set1.add(10)
print("after add function: ")
print(set1)
print(len(set1))

# union function
set2 = set([11, 12, 13, 14])
print("after union function: ")
print(set1.union(set2))
print(len(set1.union(set2)))

# intersection function
set3 = set([4, 5, 6, 12])
print("After intersection operation: ")
print(set1 & set3)
print(len(set1.intersection(set3)))

# difference function
print("After difference function: ")
print(set1.difference(set3))
print(len(set1-set3))

# difference_update function
print("after difference_update function: ")
set1.difference_update(set3)
print(set1)
print(len(set1))