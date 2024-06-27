# 9. Leap Year Checker

# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    is_leap = "a leap"
else:
    is_leap = "not a leap"

print("The year is", is_leap)