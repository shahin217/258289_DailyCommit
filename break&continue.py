# break
print("use of break")
i = 1
while True:
    print(i, end="  ")
    i += 1
    if i > 10:
        break

# continue
print("\nlist of odd numbers using continue: ")
for i in range(11):
    if i % 2 == 0:
        continue
    else:
        print(i, end="  ")
