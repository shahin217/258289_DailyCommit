my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

loop_sum = 0
for i in my_list:
    loop_sum += i

print("sum of elements using for loop= ", loop_sum)

# while loop
i = 0
loop_sum = 0
while i <= len(my_list):
    loop_sum += i
    i += 1

print("sum of elements using while loop= ", loop_sum)
