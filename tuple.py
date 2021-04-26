tup1 = (1, 2, 3, 4)
print(tup1)
print(len(tup1))

# concatenating tuples
tup2 = (5, 6, 7)
print(tup1+tup2)
print(len(tup1+tup2))

# nesting of tuples
tup3 = (tup1, tup2)
print(tup3)
print(len(tup3))

# deleting tuple
del tup3
# print(tup3)

# slicing in tuples
print("tup1[1:] = ", tup1[1:])
print("tup1[:3] = ", tup1[:3])
print("tup1[1::2] = ", tup1[1::2])
print("tup1[-3:-1] = ", tup1[-3:-1])

# converting tuple into list
print(list(tup1))

print("max in tup1 = ", max(tup1))
print("min in tup1 = ", min(tup1))