# 8. Prime Number Checker

# Problem: Check if a number is prime.

number = 13

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)