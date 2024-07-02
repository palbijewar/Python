# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and programs. It allows for data and functions to be bundled together, making code more modular, reusable, and scalable.

### Key Concepts of OOP

1. **Class**: A blueprint for creating objects.
2. **Object**: An instance of a class.
3. **Attributes**: Variables that belong to an object or class.
4. **Methods**: Functions that belong to an object or class.
5. **Inheritance**: A way to form new classes using classes that have already been defined.
6. **Encapsulation**: Bundling the data and the methods that operate on the data into a single unit or class.
7. **Polymorphism**: The ability to present the same interface for different data types.

## Classes and Objects

### Defining a Class

```python
class CoffeeMachine:
    # Class attribute
    water_level = 100

    # Constructor
    def __init__(self, brand):
        # Instance attribute
        self.brand = brand

    # Method
    def make_coffee(self):
        if self.water_level > 0:
            print(f"{self.brand} is making coffee")
            self.water_level -= 10
        else:
            print("Add more water!")

# Creating an object
machine = CoffeeMachine("Nespresso")

# Accessing attributes and methods
print(machine.brand)  # Output: Nespresso
machine.make_coffee()  # Output: Nespresso is making coffee
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

## Encapsulation

Encapsulation is the concept of restricting access to certain attributes and methods to protect the internal state of an object.

### Example:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
```

## Polymorphism

Polymorphism allows for using a unified interface to operate on different data types.

### Example:

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(shape.area())  # Output: 12 and 78.5
```

## Special Methods (Magic Methods)

Special methods, also known as magic methods, allow for the implementation of custom behavior for built-in Python operations.

### Example:

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("Python Programming", "John Doe")
print(book)  # Output: Python Programming by John Doe
print(len(book))  # Output: 17
```

## Conclusion

OOP in Python is a powerful paradigm that helps in organizing complex programs, making them more manageable, modular, and scalable. Understanding classes, objects, inheritance, encapsulation, polymorphism, and special methods are key to leveraging OOP effectively in your Python projects.