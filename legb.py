#1.
"""
def len(l):
    print("Hii")
l1=[1,3,4]
print(len(l1))
"""

#2.1 way
# c = 0

# a = int(input())

# def m1():
#     global c

#     while c <= a:
#         if c == 4:
#             print(c)
#         c += 1

# m1()

"""
c=0
def m1():
    global c
    c+=1
m1()
m1()
m1()
m1()
print(c)
"""
unsuccessful_attempts=0
successful_attempts=0
def login(name="sravani",password_value="12345"):
    global successful_attempts
    global unsuccessful_attempts
    username=input("enter a username:")
    password=input("enter a password:")
    if username==name and password==password_value:
            if successful_attempts<3:
                successful_attempts+=1
                print("Login Successful")
                print("Successful Attempts:",successful_attempts)
            else:
                 print("Successful Attempts limit Reached")
    else:
         if unsuccessful_attempts<3:
              unsuccessful_attempts+=1
              print("Login Failed")
              print("Unsuccessful Attempts:",unsuccessful_attempts)
         else:
              print("Maximum Unsuccessful Attempts Reached")
while successful_attempts<3:
     login()
              
        
    

