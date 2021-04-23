def get_second_smallest(myList):
    myList.sort()               # sorting the list
    return myList[1]            # returning second smallest element


# Driver Code
my_list = [12, 2, 38, 14, 85]
print("Second smallest element in list is ", get_second_smallest(my_list))
