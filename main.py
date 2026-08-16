#1.print("Hello World")
#2.ATM System Create a simple ATM system where the user can deposit money, withdraw money, and check the current balance.
balance = 5000

def deposit_money(amount):
    global balance
    balance += amount
    return balance

def withdraw_money(amount):
    global balance

    if amount <= balance:
        balance -= amount
        return balance
    else:
        print("Insufficient funds")
        return balance

def check_balance():
    return balance

deposit = int(input("Enter deposit amount: "))
withdraw = int(input("Enter withdraw amount: "))

deposit_money(deposit)
withdraw_money(withdraw)

print("Current Balance:", check_balance())

#Q3.Calculate Bill Create a function calculate_bill(price, quantity) that returns the total cost. Add ₹40 delivery fee if the total is less than ₹200.
def calculate_bill(price, quantity):
    total = price * quantity

    if total < 200:
        total += 40

    return total

price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print("Total Bill:", calculate_bill(price, quantity))

#Q4.Grade System Create three functions:
#total() → calculates total marks
#average() → calculates average
#grade() → returns the grade
def total(a, b, c, d, e):
    return a + b + c + d + e

def average(total_marks):
    return total_marks / 5

def grade(avg):
    if avg > 85:
        return "A Grade"
    elif avg >= 75:
        return "B Grade"
    elif avg >= 65:
        return "C Grade"
    elif avg >= 55:
        return "D Grade"
    else:
        return "Fail"

print(grade(average(total(80, 70, 90, 85, 75))))
#5. Positional & Keyword Arguments Uber Trip Details
# Create a function trip_details(driver, pickup, drop, total). Call it once using positional arguments and once using keyword arguments.
def trip_details(driver, pickup, drop, total):
    print("Driver:", driver)
    print("Pickup:", pickup)
    print("Drop:", drop)
    print("Total:", total)

# Positional arguments
trip_details("Sravani", "Vijayawada", "Hyderabad", 500)

# Keyword arguments
trip_details(
    driver="Sravani",
    pickup="Vijayawada",
    drop="Hyderabad",
    total=500
)
#6.Insurance:Create a function apply_insurance(amount, **insurance) that subtracts all insurance claims from the amount.
def apply_insurance(amount, **insurance):
    total_claim = 0

    for key, value in insurance.items():
        print(key, ":", value)
        total_claim += value

    return amount - total_claim

result = apply_insurance(
    5000,
    medical=500,
    accident=300
)

print("Final Amount:", result)
#7.Design a Python program for a supermarket billing system.
#  Create a function calculate_total(*prices) 
# that accepts the prices of multiple items 
# and returns their total cost.
#  Then define a function apply_discount(*amount) 
# that applies a 10% discount if the total exceeds 1500.
#  Finally, create a function final_bill(**details) that
#  accepts keyword arguments such as amount, tax, and packing_charge,
#  and returns the final payable bill. 
# Display the final amount using a single nested function call.
def calculate_total(*prices):
    total = sum(prices)
    return total


def apply_discount(*amount):
    total = sum(amount)

    if total > 1500:
        total = total - (total * 10 / 100)

    return total


def final_bill(**details):
    amount = details["amount"]
    tax = details["tax"]
    packing_charge = details["packing_charge"]

    return amount + tax + packing_charge


print(
    final_bill(
        amount=apply_discount(
            calculate_total(500, 400, 300, 600)
        ),
        tax=100,
        packing_charge=50
    )
)
#8.create a python application to develop a simple hospital billing system design functions
#like calculate well with positional arguement charges of variable or arbitrary type and another function applies insurance
#with keyword argueents of arbitrary type creae another function add taxes with keyword arguements or arbitrary type
#the program should accepts mutliple charges like consult,treatment,tests, apply insurance reduction and then add tax
# Calculate total hospital charges
def calculate_bill(*charges):
    total = 0

    for charge in charges:
        total += charge

    return total


# Apply insurance reduction
def apply_insurance(amount, **insurance):
    total_reduction = 0

    for key, value in insurance.items():
        print(key, "insurance:", value)
        total_reduction += value

    return amount - total_reduction


# Add taxes
def add_tax(amount, **taxes):
    total_tax = 0

    for key, value in taxes.items():
        print(key, "tax:", value)
        total_tax += value

    return amount + total_tax


# Hospital charges
total = calculate_bill(
    500,    # consultation
    2000,   # treatment
    1000    # tests
)

# Apply insurance
after_insurance = apply_insurance(
    total,
    health_insurance=500,
    medical_insurance=200
)

# Add taxes
final_amount = add_tax(
    after_insurance,
    gst=100,
    service_tax=50
)

print("Total Charges:", total)
print("After Insurance:", after_insurance)
print("Final Hospital Bill:", final_amount)

#9.create a python appliacation to design function for a food delivery application where customer name is taken as the positional arguement
#the order type is a default arguement = regular where the function should accepts multiple food items ordered by the customers
#using positional arguements and additional details such as address,payment mode,delivery instructions and discount using keyword arguements
#the function should deisplay complete summary  display the customer details, list of ordered and total no of items and all additional items

def food_delivery(customer_name, order_type="regular", *food_items, **details):

    print("----- FOOD DELIVERY SUMMARY -----")
    print("Customer Name:", customer_name)
    print("Order Type:", order_type)

    print("Ordered Items:")

    for item in food_items:
        print("-", item)

    print("Total Number of Items:", len(food_items))

    print("\nAdditional Details:")

    for key, value in details.items():
        print(key, ":", value)


food_delivery(
    "Sravani",
    "Regular",
    "Pizza",
    "Burger",
    "French Fries",
    address="Hyderabad",
    payment_mode="UPI",
    delivery_instructions="Call before delivery",
    discount="10%"
)