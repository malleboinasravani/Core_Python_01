#Keyword Arguments
#1.Call the function send_email(to, subject, body) using keyword arguments in any order.

def send_email(to,subject,body):
    print("To:",to)
    print("Subject:",subject)
    print("Body:",body)
send_email(body="Come Tomorrow",to="anchapremchand@gmail.com",subject="Interview")
#2.Write a function create_profile(username, email, age) and call it using keyword arguments.

def create_profile(username,email,age):
    print("Username:",username)
    print("Email:",email)
    print("Age:",age)
create_profile(age=23,username="Sravani",email="malleboinasravani2003@gmail.com")
#3.What is the error if you place a positional argument after a keyword argument? Test it.
# Rewrite this call using keyword arguments:
# book_ticket("Alice", "Delhi", "Mumbai", 2)
def book_ticket(name,seats,from_city,to_city):
    print("Name:",name)
    print("Seats:",seats)
    print("From_City:",from_city)
    print("To_City:",to_city)
book_ticket(to_city="Mumbai",seats=2,name="Alice",from_city="Delhi")
#4.What is the error if you place a positional argument after a keyword argument? Test it.

"""def student(name, age, city):
    print(name, age, city)

student(name="Sravani", 23, city="Hyderabad")"""

#5. Why are keyword arguments considered more readable?

#Answer:
#Keyword arguments are considered more readable because 
# they clearly show which value belongs to which parameter.
#  This makes the function call easy to understand, 
# especially when there are many parameters.

#Example:
def student(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

student(name="Sravani", age=23, city="Hyderabad")
