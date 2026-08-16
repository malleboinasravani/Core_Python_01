#Q1. Write a lambda function that takes a number and returns its cube.
cube_num = lambda x: x ** 3
print(cube_num(5))

#Q2. Create a lambda that takes two numbers and returns the larger one using a conditional expression.

larger_number = lambda x, y: x if x > y else y
print(larger_number(10, 49))

#Q3. Convert this regular function into a lambda.
#Regular function:
def even(n):
    return n % 2 == 0
#Answer:
even = lambda n: n % 2 == 0

print(even(10))
print(even(7))

#Q4. Use a lambda with sorted() to sort this list of tuples by the second element.
#Given:
list_ele = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
#Answer:
list_ele = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]

sorted_list = sorted(list_ele, key=lambda x: x[1])

print(sorted_list)

#Q5. Can a lambda function call another function inside it? Write an example.
#Yes. A lambda function can call another function.
def square(n):
    return n * n

result = lambda x: square(x)

print(result(5))

#Q6. What are the three main limitations of lambda compared to def?
"""
1.Lambda can contain only one expression.
square = lambda x: x * x
2.Lambda cannot contain multiple statements.
For example, you cannot normally write several statements
such as assignments and print() statements inside a lambda.
3.Lambda is less readable for complex logic.
For complicated functions, def is better because it allows multiple lines,
meaningful names, documentation, and easier debugging.
"""
#Q7.Write a lambda to calculate simple interest.
#Formula: (P * R * T) / 100

simple_interest = lambda p, r, t: (p * r * t) / 100

print(simple_interest(10000, 5, 2))

#Q8. Temperature Converter
#Write a lambda to convert Celsius to Fahrenheit.
#Formula: (C * 9/5) + 32
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

print(celsius_to_fahrenheit(25))

#Q9.Electricity Bill
#Write a lambda that calculates the bill amount:
#If units ≤ 100 → ₹5/unit
#Else → ₹8/unit

electricity_bill = lambda units: units * 5 if units <= 100 else units * 8

print(electricity_bill(80))
print(electricity_bill(150))

#Q10.Login Check
#Write a lambda that checks whether username is "admin" and password is "1234".

login = lambda username, password: (
    "Login Success"
    if username == "admin" and password == "1234"
    else "Invalid"
)

print(login("admin", "1234"))
print(login("admin", "5678"))

