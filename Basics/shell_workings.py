# # Python Shell Workings

# # Launching Python Shell
# # PS C:\Users\PAL\OneDrive\Documents\Python> python
# # Python 3.12.1 (tags/v3.12.1:2305ca5, Dec 7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
# # Type "help", "copyright", "credits" or "license" for more information.

# # Basic Python Commands
# >>> print("hello")
# # Output: hello

# >>> print(9 + 10)
# # Output: 19

# >>> 4 * 8
# # Output: 32

# >>> "chai" * 4
# # Output: 'chaichaichaichai'

# >>> "chai " * 4
# # Output: 'chai chai chai chai '

# # Working with Variables
# >>> score = 100
# >>> score
# # Output: 100

# # NameError Example
# >>> tea
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # NameError: name 'tea' is not defined

# # ModuleNotFoundError Example
# >>> import coffee
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # ModuleNotFoundError: No module named 'coffee'

# # Using the os module
# >>> import os
# >>> os.getcwd()
# # Output: 'C:\\Users\\PAL\\OneDrive\\Documents\\Python'

# # For Loop Example with Indentation Error
# >>> for c in "coffee":
# ... print(c)
# # File "<stdin>", line 2
# #     print(c)
# #     ^
# # IndentationError: expected an indented block after 'for' statement on line 1

# # Corrected For Loop
# >>> for c in "coffee":
# ...     print(c)
# ...
# # Output:
# # c
# # o
# # f
# # f
# # e
# # e

# # Using the sys module
# >>> import sys
# >>> sys.platform
# # Output: 'win32'

# # Importing a Custom Module
# >>> import hello_world
# # Output:
# # Hello world
# # 4

# # Re-importing the same module has no additional output
# >>> import hello_world
# >>> import hello_world
# >>> import hello_world

# # ModuleNotFoundError Example for a Non-Existent Submodule
# >>> import hello_world.coffee_one
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # ModuleNotFoundError: No module named 'hello_world.coffee_one'; 'hello_world' is not a package

# # AttributeError Example
# >>> hello_world.coffee_one
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: module 'hello_world' has no attribute 'coffee_one'

# # Using importlib to reload a module
# >>> from importlib import reload
# >>> reload(hello_world)
# # Output:
# # Hello world
# # 4
# # <module 'hello_world' from 'C:\\Users\\PAL\\OneDrive\\Documents\\Python\\Basics\\hello_world.py'>

# # Accessing an Attribute after reloading the module
# >>> hello_world.coffee_one
# # Output: 'latte'
