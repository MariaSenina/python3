# Data Types

# Integer -> int

# Float -> float

# Boolean -> bool

# String -> str
print(type("Hello"))

username = "supercoder"
password = "supersecret"

some_long_string = '''
WOW
O O
---
'''

print(some_long_string)

name = input("What is your name? ")
year = input("What year were you born? ")

age = 2022 - int(year)

print(f'Hi {name}! You are {age} years old. \n')

greeting = "Hello, Python!"
print(greeting)
print("This is the 1st letter: " + greeting[0])
print("This is the 5th letter: " + greeting[4])
print("This is the range of letters from 1 UNTIL 5: " + greeting[0:4])
# [start:stop:step_over] -> NOTE: we can skip any part of this expression (defaults - 0:<end>:1)
print("This is the range of letters with step_over: " + greeting[0:15:2])
# negative index means "start at the end" (starts at -1)
print("This is the last character: " + greeting[-1])
# reverse string -> [::-1]
print("This is the reversed string: " + greeting[::-1])

# List -> list

# Tuple -> tuple

# Set -> set

# Dictionary -> dict


#Null? -> None