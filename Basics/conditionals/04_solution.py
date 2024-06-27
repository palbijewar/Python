# 4. Fruit Ripeness Checker

# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Apple"
color = "Green"

if color != "Green" and color != "Yellow" and color != "Brown":
    print("You can only choose color between green, yellow and brown")
    exit()

if fruit != "Banana":
    print("This check is only for Banana")
    exit()

if fruit == "Banana":
    if color == "Green":
        fruit_is = "Unripe"
    elif color == "Yellow":
        fruit_is = "Ripe"
    elif color == "Brown":
        fruit_is = "Overripe"

print("Fruit is:", {fruit_is})