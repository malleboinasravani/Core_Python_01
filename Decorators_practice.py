#Q1.⁠⁠Create functions add(a, b), subtract(a, b) and multiply(a, b).

# Create a function calculate(operation, a, b) that accepts a function reference and performs the selected operation.

# Use lambda functions to perform:

# •⁠  ⁠Square of a number
# •⁠  ⁠Cube of a number
# •⁠  ⁠Double of a number

# Add a decorator log_operation that prints "Operation started" before execution and "Operation completed" after execution.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
square=lambda x:x*x
cube=lambda x:x**3
double=lambda x:x*2
def log_operation(func):
    def wrap1(*args,**kwargs):
        print("Operation Started")
        result=func(*args,**kwargs)
        print("Operation Completed")
        return result
    return wrap1
@log_operation
def calculate_operation(operation,a,b):
    return operation(a,b)
print(calculate_operation(add,10,89))
print(calculate_operation(sub,678,89))
print(calculate_operation(mul,23,90))
print(square(9))
print(cube(9))
print(double(9))


# Q2.Create a function process_marks(marks, operation) where operation is a function reference.

# Use lambda functions to:

# •⁠  ⁠Add 5 grace marks
# •⁠  ⁠Double each mark
# •⁠  ⁠Find whether a mark is greater than 40

# Create a decorator that prints "Processing started" and "Processing completed"

def decorator1(func):
    def wrapper1(*args,**kwargs):
        print("Processing Started")
        result=func(*args,**kwargs)
        print("Processing Completed")
        return result
    return wrapper1
@decorator1
def process_marks(marks,operation):
    res=[]
    for mark in marks:
        res.append(operation(mark))
    return res
marks=[1000,60,59,23]
print(process_marks(marks,lambda x:x+5))
print(process_marks(marks,lambda x:x*2))
print(process_marks(marks,lambda x:x>40))

#Q3.Create a function process_order(price, discount_function).
# Pass different lambda functions to calculate:
# 10% discount
# 20% discount
# ₹100 flat discount
# Create two decorators:
# order_logger → logs the order processing
# payment_check → prints "Payment verification completed"
# Apply both decorators to the function.

def order_logger(func):
    def wrapper1(price,discount_function):
        print("Order Processing Started")
        result=func(price,discount_function)
        print("Order Processing Completed")
        return result
    return wrapper1
def payment_check(func):
    def wrapper2(price,discount_function):
        print("Payment Verification Completed")
        return func(price,discount_function)
    return wrapper2
@order_logger
@payment_check
def process_order(price,discount_function):
    final_price=discount_function(price)
    print("Price:",price)
    print("Final Price:",final_price)

discount10=lambda price:price-(price*10/100)
discount20=lambda price:price-(price*20/100)
discount100=lambda price:price-100
process_order(1000,discount10)
process_order(1000,discount20)
process_order(1000,discount100)

# 4 . Create a function send_notification(message, formatter).

# Use lambda functions as formatter to:

# •⁠  ⁠Convert the message to uppercase
# •⁠  ⁠Convert the message to lowercase
# •⁠  ⁠Add "!!!" to the message

# Create a decorator that prints "Notification started" 
# before execution and "Notification sent" after execution.

def notification_decorator(func):
    def wrapper1(*args, **kwargs):
        print("Notification Started")
        result = func(*args, **kwargs)
        print("Notification Sent")
        return result
    return wrapper1


@notification_decorator
def send_notification(message, formatter):
    return formatter(message)


uppercase = lambda msg: msg.upper()
lowercase = lambda msg: msg.lower()
add_exclamation = lambda msg: msg + "!!!"


print(send_notification("sravani Malleboina", uppercase))
print(send_notification("sravaNi mAlleBOIna", lowercase))
print(send_notification("Sravani Malleboina", add_exclamation))
#5.⁠Create a function transaction(amount, operation).

# Pass different functions as operation:

# •⁠  ⁠Deposit
# •⁠  ⁠Withdrawal
# •⁠  ⁠Balance update

# Use a decorator to log every transaction.

# Create another decorator that checks whether the transaction 
# amount is greater than 0.

# Use two decorators together. ‎<This message was edited>

def deposit(amount):
    print(f"Deposited:₹{amount}")
def withdrawal(amount):
    print(f"Withdraw:₹{amount}")
def balance_update(amount):
    print(f"Balance Updated by:₹{amount}")

def log_transaction(func):
    def wrapper1(amount,operation):
        print("Transaction Started")
        result=func(amount,operation)
        print("Transaction Completed")
        return result
    return wrapper1
def check_amount(func):
    def wrapper2(amount,operation):
        if amount>0:
            return func(amount,operation)
        else:
            print("Invalid transaction amount")
    return wrapper2
@log_transaction
@check_amount
def transaction(amount,operation):
    operation(amount)
transaction(10002,deposit)
transaction(12344,withdrawal)
transaction(16389,balance_update)
transaction(-1780,deposit)
