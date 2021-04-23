tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)

print("repeated elements in tuple: ")

for i in tup:
    if tup.count(i) > 1:
        print(i)
