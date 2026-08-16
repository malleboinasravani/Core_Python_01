#What are arbitrary parameters?
"""
Arbitrary parameters are used when we don't know in advance how many arguments a function will receive.
Python provides:
*args → any number of positional arguments
**kwargs → any number of keyword arguments
"""
#1. *args
#*args collects multiple positional arguments into a tuple.
def add_all(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add_all(10, 20))
print(add_all(10, 20, 30, 40))

#2. **kwargs
#**kwargs collects multiple keyword arguments into a dictionary.
def person_info(**kwargs):
    print(kwargs)

person_info(name="Sravani", age=23, city="Hyderabad")

#Q3.Write a function multiply_all(*args) that returns the product of all numbers passed.
def multiply_all(*args):
    product = 1

    for num in args:
        product *= num

    return product


print(multiply_all(1, 2, 3))
print(multiply_all(2, 3, 4, 5))

#Q4. Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line.
def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_tags(name="Sravani", age=23, city="Hyderabad")

#Q5. Write a function describe_person(name, *hobbies) where name is a regular parameter and hobbies are collected into a tuple.
def describe_person(name, *hobbies):
    print("Name:", name)
    print("Hobbies:", hobbies)


describe_person("Sravani", "Reading", "Coding", "Music")

#Q6. What is the output of this code?
def f(*args):
    print(type(args))


f(1, 2, 3)
#Q7. Write a function create_html_tag(tag, **attributes) that prints <tag key='val' ...>.
#Example:
#create_html_tag('a', href='https://python.org', target='_blank')
#Answer:
def create_html_tag(tag, **attributes):
    result = "<" + tag

    for key, value in attributes.items():
        result += f" {key}='{value}'"

    result += ">"
    
    print(result)


create_html_tag(
    'a',
    href='https://python.org',
    target='_blank'
)

#Q8. Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print each part.
#Answer:
def mixed(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


mixed(10, 20, 30, 40, 50, city="Hyderabad", age=23)

#Q9.Create a function student_info(name, *subjects, **details) 
# that prints a student's name, subjects enrolled,
#  and additional details like grade and school.
def student_info(name, *subjects, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Details:", details)

student_info(
    "Sravani",
    "Python",
    "SQL",
    "HTML",
    grade="A",
    school="Vignan"
)
#Q10.Write a function order_food(*items, **preferences) 
# that accepts multiple food items and optional preferences
#  like spice level or delivery time.

def order_food(*items, **preferences):
    print("Food Items:", items)
    print("Preferences:", preferences)

order_food(
    "Pizza",
    "Burger",
    "Biryani",
    spice_level="medium",
    delivery_time="8 PM"
)
#Q11.Write a function shopping_cart(discount=0, *prices)
#  that calculates the total price after applying a discount.

def shopping_cart(discount=0, *prices):
    total = sum(prices)
    final_price = total - (total * discount / 100)
    return final_price

print(shopping_cart(0, 100, 200, 300))
print(shopping_cart(10, 100, 200, 300))

#Q12.Design a function register_user(username, role="user", *permissions, **details) that stores user information.

def register_user(username, role="user", *permissions, **details):
    user = {
        "username": username,
        "role": role,
        "permissions": permissions,
        "details": details
    }

    return user

result = register_user(
    "sravani",
    "admin",
    "read",
    "write",
    "delete",
    age=23,
    city="Hyderabad"
)

print(result)

#Q13.Write a function calculate_score(base_score=0, *bonus_points, **penalties) that computes a final score.

def calculate_score(base_score=0, *bonus_points, **penalties):
    final_score = base_score

    for bonus in bonus_points:
        final_score += bonus

    for penalty in penalties.values():
        final_score -= penalty

    return final_score

result = calculate_score(
    50,
    10,
    5,
    late=3,
    mistake=2
)

print("Final Score:", result)

#Q14.Design a function send_email(sender, receiver, subject="No Subject", *attachments, **options) that simulates sending an email.

def send_email(sender, receiver, subject="No Subject",
               *attachments, **options):

    print("Sender:", sender)
    print("Receiver:", receiver)
    print("Subject:", subject)
    print("Attachments:", attachments)
    print("Options:", options)

send_email(
    "sravani@gmail.com",
    "company@gmail.com",
    "Job Application",
    "resume.pdf",
    "certificate.pdf",
    priority="high",
    cc="hr@gmail.com"
)

#Q15.Write a function shopping_cart(discount=0, *prices) 
# that calculates the total price after applying a discount.
def shopping_cart(discount=0, *prices):
    total = sum(prices)
    final_price = total - (total * discount / 100)
    return final_price


print(shopping_cart(0, 100, 200, 300))
print(shopping_cart(10, 100, 200, 300))

#Q16.Design a function 
# register_user(username, role="user", *permissions, **details) 
# that stores user information.
def register_user(username, role="user", *permissions, **details):
    user = {
        "username": username,
        "role": role,
        "permissions": permissions,
        "details": details
    }

    return user


result = register_user(
    "sravani",
    "admin",
    "read",
    "write",
    "delete",
    age=23,
    city="Hyderabad"
)

print(result)

#Q17.Write a function calculate_score(base_score=0, *bonus_points, **penalties) 
# that computes a final score after adding bonuses and subtracting penalties.
def calculate_score(base_score=0, *bonus_points, **penalties):
    final_score = base_score

    for bonus in bonus_points:
        final_score += bonus

    for penalty in penalties.values():
        final_score -= penalty

    return final_score


result = calculate_score(
    50,
    10,
    5,
    late=3,
    mistake=2
)

print("Final Score:", result)

#Q18.