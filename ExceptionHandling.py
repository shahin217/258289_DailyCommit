# ZeroDivisionError
try:
    a = int(input("enter value1: "))
    b = int(input("enter value2: "))
    c = a/b
except ZeroDivisionError:
    print("error occurred\ndivision by zero!")
else:
    print("division result is ", c)

# IndexError
my_list = [1, 2, 3, 4, 5, 6]
try:
    ind = int(input("enter index to access element: "))
    print("list element = ", my_list[ind])
except IndexError:
    print("error occurred\nIndex doesn't exist!")
finally:
    print("finally block is executed")
