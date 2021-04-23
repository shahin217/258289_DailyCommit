pizza_slices = int(input("How many slices do you want:\n"))

total_price = 0
if pizza_slices % 2 == 0:
    total_price = 120.00 * pizza_slices
else:
    total_price = 123.00 * pizza_slices

print("Total charges :", total_price)
