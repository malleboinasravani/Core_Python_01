# What is a Decorator?
"""A decorator is a function that is used to modify or extend the behavior of another function without changing its original code.
In simple words:
A decorator adds extra functionality to an existing function.
"""
#Example:
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@decorator
def say_hello():
    print("Hello")
say_hello()


#1.Create a function get_message() that returns "hello user".
# Write a decorator using @ syntax
# that converts the output to uppercase
def uppercase_decorator(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper
@uppercase_decorator
def get_message():
    return "hello world"
print(get_message())


#2. Create a function get_number() that
# returns 10 Use a decorator to return double the value.
def number(func):
    def wrapper():
        result=func()
        return result*2
    return wrapper
@number
def get_number():
    return 10
print(get_number())

#3.Create a function place_order(item)
# Use a decorator to print:
# * “Order process started”
# * “Order process completed”
def order_decorator(func):
    def wrapper(item):
        print("Order process started")
        func(item)
        print("Order process completed")
    return wrapper


@order_decorator
def place_order(item):
    print("Order placed:", item)
place_order("Pizza")

#4. Create a function login(username)
    # Use a decorator to print:
    # * “Authenticating user…”
# * “Login successful”
def decorator(func):
    def wrapper(username):
        print("Authenticating user")
        func(username)
        print("Login successful")
    return wrapper
@decorator
def login(username):
    print("Username:",username)
print("Sravani")

#5.   Create a function send_message(msg)
# Use a decorator to print:
# * “Sending message…”
# * “Message sent”
def decorator(func):
    print("Sending message")
    def wrapper(msg):
        print("Message sent")
        func(msg)
    return wrapper
@decorator
def send_message(msg):
    print("Message:",msg)
print("Hii,Sravani")

#6.Create a function add(a, b)
# Use a decorator to print:
# * “Calculating sum…”
# * “Calculation done”
def decorator(func):
    print("Calculating sum......")
    def wrapper(a,b):
        result=func(a,b)
        print("Calculation done")
        return result
    return wrapper
@decorator
def add(a,b):
    return a+b
print(add(10,40))

# 7.Create a function apply_discount(price)
#     Use a decorator to print:
#     * “Applying discount…”
#     * “Discount applied”
def discount_decorator(func):
    def wrapper(price):
        print("Applying discount...")
        result = func(price)
        print("Discount applied")
        return result
    return wrapper


@discount_decorator
def apply_discount(price):
    return price * 0.90


print(apply_discount(100))

#8. Create a function place_order(item)
# Write a decorator that prints:
# * “Function started” before execution
# * “Function ended” after execution
def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("Function Started")
        func(*args,**kwargs)
        print("Function ended")
    return wrapper1
@decorator1
def place_order(item):
    print("Item:",item)
place_order("Pizza")

#9. Create a function greet(name)
# Write a decorator that adds:
# * “Welcome!” before
# * “Have a nice day!” after
def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("Welcome!")
        func(*args,**kwargs)
        print("Have a nice day!")
    return wrapper1
@decorator1
def greet(name):
    print(name)
greet("Sravani")

#10.Create a function transfer_money()
# Write a decorator that prints:
# * “Transaction started”
# * “Transaction successful” / “Transaction failed”
def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("Transaction Started")
        func(*args,**kwargs)
        print("Transaction successful")
    return wrapper1
@decorator1
def transfer_money():
    print("Money Transferred successful")
transfer_money()

#11.Create a function start_system()
# Write a decorator that prints:
# * “System starting…” before execution
# * “System started successfully” after execution
def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("System Starting.....")
        func(*args,**kwargs)
        print("System started successfully")
    return wrapper1
@decorator1
def start_system():
    print("System is Running")
#12. Create a function show_message()
# Write a decorator that prints:
# * “Welcome!” before
# * “Goodbye!” after
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("Welcome!")
        func(*args,**kwargs)
        print("Goodbye!")
    return wrapper
@decorator1
def show_message():
    print("Hello")
show_message()

#13.Create a function make_payment()
# Write a decorator that prints:
# * “Payment initiated” * “Payment successful”
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("Payment initiated")
        func(*args,**kwargs)
        print("Payment successful")
    return wrapper
@decorator1
def make_payment():
    print("Making payment........")
make_payment()

#14.Create a decorator and check the name of the decorated function.
def decorator1(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper
@decorator1
def method1():
    print("hello")

print(method1.__name__)

#15.banking application has a function check_balance().
# Create two decorators: verify_user,
# which prints "User verified", and log_transaction,
# which prints "Transaction logged".
# Apply both decorators to check_balance()
#and display "Balance displayed" from the original function.
def verify_user(func):
    def wrapper1():
        print("User Verified")
        func()
    return wrapper1
def log_transaction(func):
    def wrapper2():
        print("Transaction Logged")
        func()
    return wrapper2
@verify_user
@log_transaction
def check_balance():
    print("Balance displayed")
check_balance()

#16.An online examination system has a function start_exam(student).
# Before allowing the student to start the exam,
# the system must verify the student’s login and
# then log the exam activity.
# Create two decorators, login_required
# and log_activity, and apply both decorators to start_exam().
# The function should finally display
# "Exam started for <student>".

def login_required(func):
    def wrapper1(student):
        print("Login Verified")
        func(student)
    return wrapper1
def log_activity(func):
    def wrapper2(student):
        print("Exam activity logged")
        func(student)
    return wrapper2
@login_required
@log_activity
def start_exam(student):
    print("Exam started for",student)
start_exam("Sravani")

#17.An online shopping application has a function place_order().
# Create two decorators: login_check to print "Login verified"
# and order_log to print "Order recorded".
# Apply both decorators to place_order() and display
# "Order placed successfully" from the original function

def login_check(func):
    def wrapper1():
        print("Login Verified")
        func()
    return wrapper1
def order_log(func):
    def wrapper2():
        print("Order recorded")
        func()
    return wrapper2
@login_check
@order_log
def place_order():
    print("Order placed successfully")
place_order()

#18.--1st way:Calling a Function Normally
def greet(name):
    print("my name is",name)
def m1():
    print("hi!")
m1()
greet("premchand")
#19.2nd wayyyy:Passing a Function as an Argument
def m1(func):
    print("hii!")
    func("sravani")
m1(greet)

#20.Creating and Applying a Decorator Manually,with @ Syntax
#The same thing can be written more easily using @:
def decorator1(func):
    def wrapper1():
        print("hii!")
        func()
    return wrapper1
def intro():
    print("This is py-20")
modify=decorator1(intro)
modify()
from curses import wrapper

#21.Applying One Decorator to Multiple Functions
def decorator1(func):
    def wrapper():
        print("Welcome")
        func()
    return wrapper

def add():
    print("Adding")
def sub():
    print("subtracting")

add = decorator1(add)
sub=decorator1(sub)

add()
# sub()


#22.Create a function place_order(item).
# Write a decorator that prints:
# * “Function started” before execution
# * “Function ended” after execution

def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("Function Started")
        func(*args,**kwargs)
        print("Function ended")
    return wrapper1
@decorator1
def place_order(item):
    print("Item:",item)
place_order("Pizza")


#Q23. System Starting Decorator
#  Create a function start_system(). Write a decorator that prints:
# "System starting..." before execution
# "System started successfully" after execution

def dec1(func):
    def wrapper1():
        print("System starting...")
        func()
        print("System started successfully")
    return wrapper1


def start_system():
    print("System is Running")


start_system = dec1(start_system)

start_system()
#Q24.Create a function show_message(). Write a decorator that prints:
# "Welcome!" before
# "Goodbye!" after
def dec1(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Goodbye!")
    return wrapper


def show_message():
    print("Showing a Message")


show_message = dec1(show_message)

show_message()

#Q25. Payment Decorator Create a function make_payment(). Write a decorator that prints:
# "Payment initiated"
# "Payment successful"
def dec1(func):
    def wrapper():
        print("Payment initiated")
        func()
        print("Payment successful")
    return wrapper


def make_payment():
    print("Payment")


make_payment = dec1(make_payment)

make_payment()
#Q26. Place Order Decorator Create a function place_order(item). Write a decorator that prints:
#"Function started" before execution
#"Function ended" after execution

def dec1(func):
    def wrapper1(item):
        print("Function started")
        func(item)
        print("Function ended")
    return wrapper1


def place_order(item):
    print("Item:", item)


place_order = dec1(place_order)

place_order("Pizza")

#Q27. Decorator with *args and **kwargs Create a function add(a, b) and write a decorator that prints "Before Calling" before execution and "After Calling" after execution.

def dec1(func):
    def wrapper1(*args, **kwargs):
        print("Before Calling")
        result = func(*args, **kwargs)
        print("After Calling")
        return result
    return wrapper1


def add(a, b):
    return a + b


x = dec1(add)

print(x(10, 20))

