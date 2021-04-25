my_list = [12, 45, 76, 34, 89, 9, 65, 54]

# length of the list
length = len(my_list)
print(my_list)
print(length)

# adding elements at the end using append
my_list.append(23)
my_list.append(68)
my_list.append(27)
print(my_list)
print(len(my_list))

# adding elements using insert
my_list.insert(0, 0)
my_list.insert(1, 1)
my_list.insert(2, 2)
print(my_list)
print(len(my_list))

# adding elements at the end using extend
my_list.extend([90, 91, 95, 98, 100])
print(my_list)
print(len(my_list))

# removing elements from the list
my_list.remove(0)
my_list.remove(9)
my_list.remove(23)
my_list.remove(27)
print(my_list)
print(len(my_list))

# negative indexing
print(my_list[-1])
print(my_list[-2])

# slicing
new_list = my_list[1:7]
print("new list after slicing 1")
print(new_list)
print(len(new_list))

new_list = my_list[1:7:2]
print("new list after slicing 2")
print(new_list)
print(len(new_list))

new_list = my_list[::-1]
print("new list after slicing 3")
print(new_list)
print(len(new_list))

new_list = my_list[-7:-1]
print("new list after slicing 4")
print(new_list)
print(len(new_list))

new_list = my_list[:7]
print("new list after slicing 5")
print(new_list)
print(len(new_list))

# list comprehension
even_number = [x for x in range(1, 11) if x % 2 == 0]
print("Even number list")
print(even_number)
print(len(even_number))

# max from even number list
print("max from even number list ", max(even_number))

# min from even number list
print("min from even number list ", min(even_number))

# sum of even number list
print("sum of even number list ", sum(even_number))