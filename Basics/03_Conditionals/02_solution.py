# 2. Movie Ticket Pricing

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

day = "wednesday"
age = 24

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
    print("Price is {price}")
else:
    print("Price is {price}")
