#DEFAULT PARAMETERS
"""A default parameter provides a value automatically when the caller does not provide one, 
while still allowing the caller to override it.
"""
#Q1. Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments.
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

#Q2. Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.
def connect(host, port=3306, protocol="TCP"):
    print(f"Host: {host}, Port: {port}, Protocol: {protocol}")


connect("localhost")
connect("localhost", 8080)
connect("localhost", 8080, "UDP")
connect("localhost", protocol="HTTP")

#Q3. What is the SyntaxError in def func(name='Guest', age)? Fix it.
"""
#Incorrect:
def func(name="Guest", age):
    pass
#Error:
#SyntaxError: non-default argument follows default argument

#A non-default parameter cannot come after a default parameter.
#Wrong:

#def func(name="Guest", age):

#Correct:
def func(age, name="Guest"):
    print(name, age)
"""
#Q4. Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument.
def discount_price(price, discount=10):
    return price - (price * discount / 100)


print(discount_price(1000))
print(discount_price(1000, 20))

#Q5. Why would you use a default parameter instead of just hardcoding a value inside the function?
#Answer:
#A default parameter provides a flexible default value that can easily be changed by the caller when needed.
#For example:
def greet(name, language="English"):
    print(f"Hello {name}, language: {language}")


greet("Sravani")
greet("Sravani", "Telugu")

#Q6.Write a function simple_interest(principal, rate=5, time=1).
def simple_interest(principal, rate=5, time=1):
    interest = (principal * rate * time) / 100
    return interest


print(simple_interest(10000))
print(simple_interest(10000, 8))
print(simple_interest(10000, 8, 2))

#Q7.Define a function login(username, password="1234").
#  Demonstrate how default arguments work and explain a potential 
# issue with using default passwords.
def login(username, password="1234"):
    print("Username:", username)
    print("Password:", password)

login("Sravani")
login("Sravani", "5678")
#Q8.Write a function area(length, breadth=None) that
#  calculates the area of a rectangle.
#  If breadth is not provided, assume it is a square.

def area(length, breadth=None):
    if breadth is None:
        breadth = length

    return length * breadth

print(area(10, 5))
print(area(10))

#Q9.