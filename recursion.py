# factorial of a number using recursion
def find_fact(n):
    if n == 1 or n == 0:
        return 1
    return n * find_fact(n - 1)


n = int(input("Enter the number to find factorial: "))
factorial = find_fact(n)
print("factorial is ", factorial)
