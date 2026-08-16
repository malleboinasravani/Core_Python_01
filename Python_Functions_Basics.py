#1.Write a function named say_hello() that prints "Welcome to Python!"
def say_hello():
    print("Welcome to Python")
say_hello()

#2.Write a function named display_name() that prints your name.
def display_name():
    name=input("What is your name?")
    print(name)
display_name()

#3.Write a function named add(a, b) that returns the sum of two numbers.
def sum_of_two_numbers(a,b):
    return a+b
print(sum_of_two_numbers(3,4))

#4.Write a function named area_of_rectangle(length, width) that returns the area of a rectangle
def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(6,4))
"""
#Q28. Function Annotations
# It is about Function Annotations / Type Hints.

#Function Annotations
#Example 1:
def integers(a: str):
    return str(a) * 2

print(integers(2.8))

Here:
a: str
is a type annotation.
It does not force Python to accept only strings.
Example 2
def greet(name: str):
    return name

print(greet("Sravani"))

Example 3:
def add(a: int, b: int):
    return a + b

print(add(10, 20))

Here:
a: int
b: int
are type annotations.
You can also specify the return type:
def add(a: int, b: int) -> int:
    return a + b
    """