def change(my_list):
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return my_list


my_list = [0, 1, 2, 3, 4, 5]
print("Before changes ", my_list)
print("After changes  ", change(my_list))
