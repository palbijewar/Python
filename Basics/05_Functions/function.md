# Functions in Python

## Introduction to Functions

Functions are reusable blocks of code that perform a specific task. They help in making the code modular, readable, and easier to maintain.

### Defining a Function

You can define a function using the `def` keyword followed by the function name and parentheses `()`.

#### Syntax:
```python
def function_name(parameters):
    # code block
    return value
```

#### Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Calling a Function

To call a function, use the function name followed by parentheses `()` and provide any required arguments.

#### Example:
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## Parameters and Arguments

### Positional Arguments

Arguments are passed to the function based on their position.

#### Example:
```python
def subtract(a, b):
    return a - b

print(subtract(10, 5))  # Output: 5
```

### Keyword Arguments

Arguments are passed using the name of the parameter.

#### Example:
```python
def divide(a, b):
    return a / b

print(divide(a=10, b=2))  # Output: 5.0
```

### Default Arguments

You can define default values for parameters.

#### Example:
```python
def multiply(a, b=2):
    return a * b

print(multiply(5))  # Output: 10
print(multiply(5, 3))  # Output: 15
```

### Variable-Length Arguments

You can use `*args` and `**kwargs` to pass a variable number of arguments.

#### Example with `*args`:
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
```

#### Example with `**kwargs`:
```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
```

## Return Statement

The `return` statement is used to return a value from a function.

#### Example:
```python
def square(x):
    return x ** 2

print(square(4))  # Output: 16
```

## Scope of Variables

Variables defined inside a function are local to that function. Variables defined outside any function are global.

#### Example:
```python
global_var = "I am global"

def func():
    local_var = "I am local"
    print(global_var)
    print(local_var)

func()
# Output:
# I am global
# I am local
```

## Lambda Functions

Lambda functions are small anonymous functions defined using the `lambda` keyword.

#### Syntax:
```python
lambda arguments: expression
```

#### Example:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7
```

## Built-in Functions and User-defined Functions

### Built-in Functions

Python comes with many built-in functions like `print()`, `len()`, `sum()`, etc.

#### Example:
```python
print(len("Hello"))  # Output: 5
print(sum([1, 2, 3, 4]))  # Output: 10
```

### User-defined Functions

Functions defined by the user to perform specific tasks.

#### Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

## Docstrings

Docstrings are used to document the purpose of a function. They are written as the first statement in the function.

#### Example:
```python
def add(a, b):
    """
    This function adds two numbers.
    """
    return a + b

print(add(2, 3))  # Output: 5
print(add.__doc__)
```

## Function Annotations

Function annotations provide a way of associating various parts of a function with arbitrary python expressions at compile time. They can be used to provide type hints.

#### Example:
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # Output: 5
```

## Higher-Order Functions

Functions that take other functions as arguments or return them as results.

#### Example:
```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x ** 2

print(apply_function(square, 4))  # Output: 16
```

## Conclusion

Functions are a crucial part of Python programming. They allow you to write reusable and modular code, making your programs easier to read and maintain. Understanding how to define, call, and use functions effectively is essential for any Python programmer.