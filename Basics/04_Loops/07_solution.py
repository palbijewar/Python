# 7. Validate Input

# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter value b/w 1 to 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number")

# Terminal :
# Enter value b/w 1 to 10: 34
# Invalid number
# Enter value b/w 1 to 10: 56
# Invalid number
# Enter value b/w 1 to 10: 3
# Thanks