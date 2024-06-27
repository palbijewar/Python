# 10. Pet Food Recommendation

# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = "Dog"
age = 5

if species == "Dog" and age < 2:
    food = "Puppy food"
elif species == "Dog" and age >= 2:
    food = "Adult dog food"
elif species == "Cat" and age > 5:
    food = "Senior cat food"
elif species == "Cat" and age <= 5:
    food = "Adult cat food"
else:
    food = "Unknown food"

print(food)
