```markdown
# Numbers Data Type in Python

## Basic Arithmetic Operations
```python
x = 234
y = 654
z = 902

x + y
# Output: 888

x ** 2
# Output: 54756

x + y * z
# Output: 590142

(x + y) * z
# Output: 800976

x + (y * z)
# Output: 590142

20 + 2.34
# Output: 22.34

float(2.54)
# Output: 2.54

int(90)
# Output: 90

x, y, z
# Output: (234, 654, 902)

x + 1, y + 9 
# Output: (235, 663)

y % 2
# Output: 0

z ** 2
# Output: 813604
```

## Comparison Operations
```python
1 < 2
# Output: True

True + 1
# Output: 2

5 == 6
# Output: False

45 != 5.0
# Output: True

x, y, z
# Output: (234, 654, 902)

x < y < z
# Output: True

x < z
# Output: True

x == z
# Output: False

x < y and y < z
# Output: True

x < y or y < z
# Output: True

x < y or y > z
# Output: True

x < y and y > z
# Output: False

1 == 2 < 3
# Output: False

1 == True
# Output: True

1 == 2 and 2 < 3
# Output: False
```

## Math Module
```python
import math

math.floor(3.5)
# Output: 3

math.floor(-3.5)
# Output: -4

math.trunc(2.8)
# Output: 2

math.trunc(-2.8)
# Output: -2
```
Note: `floor` gives the closest lower integer value, while `trunc` truncates the value towards zero.

## Complex Numbers
Python supports complex numbers:
```python
2 + 1j
# Output: (2+1j)
```

## Number Bases
```python
oct(56)
# Output: '0o70'

hex(64)
# Output: '0x40'

bin(89)
# Output: '0b1011001'

int(45.354)
# Output: 45

int('45', 8)
# Output: 37

int('10000', 2)
# Output: 16
```

## Bitwise Operations
```python
x = 1

x << 2
# Output: 4

x | 2
# Output: 3

x & 2
# Output: 0
```

## Random Module
```python
import random

random.random()
# Output: 0.8183379870083158 (example output, will vary)

random.randint(1, 100)
# Output: 16 (example output, will vary)

l1 = ['coffee', 'chai', 'ginger tea']

random.choice(l1)
# Output: 'coffee' (example output, will vary)

random.shuffle(l1)
# List will be shuffled in place

l1
# Output: ['coffee', 'ginger tea', 'chai'] (example output, will vary)
```

## Floating Point Precision
```python
0.1 + 0.1 + 0.1
# Output: 0.30000000000000004

0.1 + 0.1 + 0.1 - 0.3
# Output: 5.551115123125783e-17

(0.1 + 0.1 + 0.1) - 0.3
# Output: 5.551115123125783e-17

0.1 + 0.1 + (0.1 - 0.3)
# Output: 2.7755575615628914e-17

from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Output: Decimal('0.0')
```

## Fractions Module
```python
from fractions import Fraction

myFra = Fraction(2, 7)
# Output: Fraction(2, 7)
```

## String Representation Differences
```python
repr('coffee')
# Output: "'coffee'"

str('coffee')
# Output: 'coffee'

print('coffee')
# Output: coffee
```