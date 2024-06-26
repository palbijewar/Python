# Reference and Copy in python

# Reference
A reference in Python means that a variable points to the memory location where the actual data is stored. When you assign one variable to another, both variables refer to the same data.

# Example of reference
a = [1, 2, 3]
b = a

# Both 'a' and 'b' refer to the same list
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3]

# Modifying the list using 'b'
b.append(4)

# Changes are reflected in both 'a' and 'b'
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]

# Copy
A copy in Python means creating a new object that is a duplicate of the original object. There are two types of copies: shallow copy and deep copy.

# Shallow Copy
A shallow copy creates a new object, but doesn’t create copies of nested objects. Changes to nested objects will be reflected in both the original and the copy.

import copy

# Creating a list with a nested list
original_list = [1, 2, [3, 4]]

# Creating a shallow copy
shallow_copy = copy.copy(original_list)

# Modifying the nested list in the shallow copy
shallow_copy[2][0] = 99

# Only the nested list shows the change
print(original_list)  # Output: [1, 2, [99, 4]]
print(shallow_copy)  # Output: [1, 2, [99, 4]]

In this example, modifying the nested list in shallow_copy also affects original_list because the nested list is still the same object in memory.

Deep Copy
A deep copy creates a new object and recursively copies all objects found in the original, including nested objects. Changes to the copy do not affect the original.

import copy

# Creating a list with a nested list
original_list = [1, 2, [3, 4]]

# Creating a deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in the deep copy
deep_copy[2][0] = 99

# Original list remains unchanged
print(original_list)  # Output: [1, 2, [3, 4]]
print(deep_copy)  # Output: [1, 2, [99, 4]]

In this example, modifying the nested list in deep_copy does not affect original_list because all objects are completely independent.

Summary
Reference: Both variables point to the same object. Changes in one reflect in the other.
Shallow Copy: Creates a new object but references nested objects. Changes to nested objects affect both the original and the copy.
Deep Copy: Creates a new object and recursively copies all nested objects. Changes in the copy do not affect the original.