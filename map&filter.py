def add(x):
    return x + 5


my_list = [1, 2, 3, 4, 5, 6, 7]
result = list(map(add, my_list))
print(result)                           # [6, 7, 8, 9, 10, 11, 12]

nums = [11, 12, 13, 14, 15]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)                                            # [12, 14]
