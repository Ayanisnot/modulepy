import math

num = float(input("Enter a number to find its square root :"))
if num < 0:
    print("square root is not defined for negative number")
else:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")