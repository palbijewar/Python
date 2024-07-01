# 4. Function Returning Multiple Values

# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def area_and_circumference(radius):
    area = math.pi * (radius * 2)
    cirumference = 2 * math.pi * radius
    return area, cirumference

print(area_and_circumference(34))
# (213.62830044410595, 213.62830044410595)