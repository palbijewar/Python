# 7. Function with *args

# Problem: Write a function that takes variable number of arguments and returns their sum.

def sums(*args):
    return sum(args)


print(sums(1,5,3,5,3,4,2))