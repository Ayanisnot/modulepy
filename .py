def mirrored_triangle(n):
    for i in range(1, n + 1):
        spaces = '' * (n - 1)
        letters  = 'A' * i
        print(spaces + letters)

rows = int(input("Enter the number of rows :"))

mirrored_triangle(rows)