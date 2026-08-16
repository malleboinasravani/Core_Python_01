#5.Write a function multiply(a, b, c) that returns the product of three numbers.
def multiply(a,b,c):
    return a*b*c
print(multiply(2,3,4))

#6.Create a function describe_pet(animal, name) that prints:"My [animal] is named [name]."
def describe_pet(animal,name):
    return f"My {animal} is named {name}."
print(describe_pet("Dog","Pinkyyy"))

#7.What happens if you call a function with fewer arguments than parameters? Try it and note the error.
def two_numbers(a,b):
    return a+b
print(two_numbers(2))

#8.Write a function power(base, exponent) that returns the base raised to the exponent using the ** operator.
def power_function(base,exponent):
    return base**exponent
print(power_function(2,3))

#9.Create a function full_name(first, middle, last) that returns the full name as a single string.
def full_name(first,midlle,last):
    return f"{first}{midlle}{last}"
print(full_name("1","4","3"))