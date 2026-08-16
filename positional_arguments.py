#10.Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.
def intro_person(name,city,hobby):
    return f"Hello {name},{city},{hobby}"
print(intro_person("Sravani","kolkata","coding"))

#11.Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?

def subtract(a,b):
    return a-b
print(subtract(10,3))
print(subtract(3,10))


#12.Write a function bio(first_name, last_name, age) and call it correctly using positional arguments.

def bio(first_name,last_name,age):
    return (f"Hello {first_name} {last_name} "
            f"{age}")
print(bio("Malleboina","Sravani",24))

#13.keyword
#write a function create_profile(email,username,age) call it using a keyword arguments

def create_profile(email,username,age):
    return f"{username},{"Email",email},{age}"
print(create_profile(username="Sravani",age=23,email="malleboinasravani2003@gmail.com"))


#14.call the function send_email(to,subject,body) using keyword arguments in any order

def send_email(to,subject,body):
    return f"{to},{subject},{body}"
print(send_email(body="i recently saw your company job notification im very intersting to join in your company...",to="anchapremchand",subject="applying for a job"))


#15.wall--- paint area calculations
import math
def paint_area(width,height,cover):
    area=width*height
    no_of_cans=math.ceil(area/cover)
    print(f"you will need {no_of_cans} cans")
h=int(input("enter your height in meters:"))
w=int(input("enter your width in meters:"))
coverage=7
paint_area(width=w,height=h,cover=coverage)

#16.check the number prime or  not
num=int(input("enter a number:"))
def prime_checker(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("Prime number")
    else:
        print("Not Prime number")
prime_checker(num)




