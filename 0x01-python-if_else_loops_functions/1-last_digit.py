#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = int(repr(number)[-1]
if ldigit > 5:
             print(f"Last digit of {number} is {ldigit} and is greater than 5")
elif ldigit == 0:
             print(f"Last digit of {number} is {ldigit} and is 0")
else:
             print(f"Last digit of {number} is {ldigit} and is greater than 5")
