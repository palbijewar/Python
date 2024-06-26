# Set Data Type in Python

## Basic Operations
Sets in Python are unordered collections of unique elements. Let's explore some basic set operations.

### Creating a Set
>>> setone = {1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3} 
{1, 2, 3, 4}
>>> setone | {1,3, 7}
{1, 2, 3, 4, 7}
>>> setone - {1,2,3,4}
set()
>>> type({})   
<class 'dict'>
