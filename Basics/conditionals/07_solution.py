# 7. Coffee Customization

# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee_order = "Medium"
extra_shot = False

if extra_shot:
    if coffee_order == "Small":
        order = coffee_order + " coffee with an extra shot of espresso!"
    elif coffee_order == "Medium":
        order = coffee_order + " coffee with an extra shot of espresso!"
    elif coffee_order == "Large":
        order = coffee_order + " coffee with an extra shot of espresso!"
else:
    order = coffee_order

print ("Your order is:", order)