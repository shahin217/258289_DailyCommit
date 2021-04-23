list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C', 'D']
list3 = ['a', 'b', 'c', 'd']

# printing original list
print("The original list 1 is : " + str(list1))
print("The original list 2 is : " + str(list2))
print("The original list 3 is : " + str(list3))

# Convert Lists to Nesting Dictionary
# Using list comprehension + zip()
res = [{a: {b: c}} for (a, b, c) in zip(list1, list2, list3)]

# printing result
print("The constructed dictionary : " + str(res))
