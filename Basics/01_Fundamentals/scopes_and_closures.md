# Scopes and Closures in Python

## Introduction to Scopes

A scope defines the region of a program where a variable is accessible. In Python, there are different types of scopes:

1. **Local Scope**: Variables defined inside a function.
2. **Enclosing Scope**: Variables in the local scope of enclosing functions (outer functions).
3. **Global Scope**: Variables defined at the top level of a script or module.
4. **Built-in Scope**: Names preassigned in Python, such as keywords and built-in functions.

### Example of Different Scopes

```python
# Global scope
username = "Global Coffee"

def outer_function():
    # Enclosing scope
    username = "Enclosing Coffee"
    
    def inner_function():
        # Local scope
        username = "Local Coffee"
        print(username)  # Output: Local Coffee
    
    inner_function()
    print(username)  # Output: Enclosing Coffee

outer_function()
print(username)  # Output: Global Coffee
```

## The LEGB Rule

Python resolves variable names using the LEGB rule:

- **L**ocal
- **E**nclosing
- **G**lobal
- **B**uilt-in

### Example of LEGB Rule

```python
x = "Global x"

def outer():
    x = "Enclosing x"
    
    def inner():
        x = "Local x"
        print(x)  # Output: Local x
    
    inner()
    print(x)  # Output: Enclosing x

outer()
print(x)  # Output: Global x
```

## Global and Nonlocal Keywords

### Global Keyword

The `global` keyword allows you to modify a global variable inside a function.

#### Example:

```python
x = "Global x"

def modify_global():
    global x
    x = "Modified Global x"

modify_global()
print(x)  # Output: Modified Global x
```

### Nonlocal Keyword

The `nonlocal` keyword allows you to modify a variable in the enclosing (non-global) scope.

#### Example:

```python
def outer_function():
    x = "Enclosing x"
    
    def inner_function():
        nonlocal x
        x = "Modified Enclosing x"
    
    inner_function()
    print(x)  # Output: Modified Enclosing x

outer_function()
```

## Closures

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Closures are used when a nested function references a value from its enclosing scope.

### Creating a Closure

#### Example:

```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!
```

### Using Closures

Closures can be used to create function factories.

#### Example:

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(9))  # Output: 27
print(times5(3))  # Output: 15
print(times5(times3(2)))  # Output: 30
```

## Practical Use Cases of Closures

### Data Hiding

Closures can be used to hide data and create a form of encapsulation.

#### Example:

```python
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
```

### Function Decorators

Closures are often used in decorators to extend the behavior of functions.

#### Example:

```python
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

## Conclusion

Understanding scopes and closures is essential for writing effective and efficient Python code. Scopes help you manage the visibility and lifetime of variables, while closures allow you to capture and reuse the state of enclosing functions. These concepts are fundamental for advanced Python programming, including decorators, function factories, and encapsulation.