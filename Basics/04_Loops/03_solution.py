# 3. Multiplication Table Printer

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = 2
result = 0

for i in range(1, 11):
    if i == 5:
        continue
    print(n, "x", i, "=", n*i)

