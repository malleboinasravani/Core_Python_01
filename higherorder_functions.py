#Higher-Order Functions in Python
"""
A Higher-Order Function (HOF) is a function that does at least one of these:
Takes another function as an argument
Returns another function
Python commonly uses these higher-order functions:"""
#1. map()
#Used to change/transform every element.
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)


#2. filter()
#Used to select elements based on a condition.
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

#3. reduce()
#Used to combine all elements into one result.

from ast import Add
from functools import reduce
from logging import Filter
from tokenize import Number

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

#4. sorted() with lambda
#Used to sort according to a particular value.
students = [
    ("Sravani", 23),
    ("Anu", 20),
    ("Ravi", 25)
]

result = sorted(students, key=lambda x: x[1])

print(result)

#5. Passing a function as an argument
#This is the most important concept of higher-order functions.
def calculate(a, b, operation):
    return operation(a, b)

result = calculate(10, 20, lambda x, y: x + y)

print(result)

#6. map() — Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)

#7. filter() — Words starting with capital letters
words = ["Apple", "banana", "Cherry", "dog", "Elephant"]

capital_words = list(filter(lambda word: word[0].isupper(), words))

print(capital_words)

#8. reduce() — Product of all numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)

#9. sorted() + lambda — Age descending
people = [
    ("Sravani", 23),
    ("Premchand", 24),
    ("Ravi", 22),
    ("Anu", 25)
]

result = sorted(people, key=lambda x: x[1], reverse=True)

print(result)

#10. filter() + map() — Even numbers and squares
#From [1..10], first remove odd numbers, then square the remaining even numbers.
numbers = list(range(1, 11))

result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)

#11. Create your own map() → my_map()
def my_map(func, lst):
    result = []

    for item in lst:
        result.append(func(item))

    return result


numbers = [1, 2, 3, 4, 5]

print(my_map(lambda x: x * 2, numbers))
print(list(map(lambda x: x * 2, numbers)))

#12. Given a list of tuples (name, marks), sort the list:
#First by marks (descending)
#Then by name (ascending)

students = [
    ("Sravani", 85),
    ("Prem", 90),
    ("Geethu", 85),
    ("Akki", 90)
]

result = sorted(students, key=lambda x: (-x[1], x[0]))

print(result)
#13.Given a list of strings, sort them based on:
# Length of the string  # Then alphabetically
words = ["cat", "apple", "dog", "bat", "elephant"]

result = sorted(words, key=lambda x: (len(x), x))

print(result)
#Q14. Given a list of words:
# Filter words that start and end with the same letter
# Convert them to lowercase
# Sort by last character, then length
# Join all words into a single string using reduce()

from functools import reduce

words = ["Apple", "Banana", "Civic", "Deed", "Level", "Orange", "Radar"]
filtered = filter(lambda word: word[0].lower() == word[-1].lower(), words)
lowercase_words = map(lambda word: word.lower(), filtered)
sorted_words = sorted(lowercase_words, key=lambda word: (word[-1], len(word)))
result = reduce(lambda x, y: x + " " + y, sorted_words)
print(result)

#15.Given a list of integers, write a program to:
#Filter numbers divisible by 2 but not by 4
#Add 3 to each using map()
#Sort the result in descending order
#Find the product of all elements using reduce()

from functools import reduce
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
filtered = filter(lambda x: x % 2 == 0 and x % 4 != 0, numbers)
mapped = map(lambda x: x + 3, filtered)
sorted_numbers = sorted(mapped, reverse=True)
product = reduce(lambda x, y: x * y, sorted_numbers)
print("Sorted result:", sorted_numbers)
print("Product:", product)

#16.Given a list of transactions where each transaction contains a type (credit or debit) and an amount, write a program to filter only the credit transactions, apply a 5% bonus to each transaction amount using map(), sort the updated transactions in descending order based on the amount, and finally compute the total credited amount using reduce().
"""INPUT: 
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]"""
from functools import reduce
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]
credits = filter(lambda x: x["type"] == "credit", transactions)
bonus_transactions = map(
    lambda x: {
        "type": x["type"],
        "amount": x["amount"] * 1.05
    },
    credits
)
sorted_transactions = sorted(
    bonus_transactions,
    key=lambda x: x["amount"],
    reverse=True
)
total = reduce(
    lambda x, y: x + y["amount"],
    sorted_transactions,
    0
)

print("Updated transactions:", sorted_transactions)
print("Total credited amount:", total)
#17.An online store stores product prices in a list.
#  Write a program using map() to apply a 10% tax 
# to each product price and display the updated prices.

prices = [100, 250, 500, 1000]

updated_prices = list(map(lambda price: price + (price * 10 / 100), prices))

print(updated_prices)

#18.A list of usernames is stored in lowercase. 
# Use map() to format them so that the first letter is uppercase.

usernames = ["sravani", "premchand", "ravi", "anusha"]

formatted = list(map(lambda name: name.capitalize(), usernames))

print(formatted)

#19.An e-commerce website wants to display 
# only products priced above ₹500. Use filter() 
# to extract those prices from a list.

prices = [250, 600, 450, 800, 1200, 300]

result = list(filter(lambda price: price > 500, prices))

print(result)

#20.Use map() with a lambda function to multiply each number in a list by 5.
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 5, numbers))

print(result)

#21.Write a program that uses map() 
# to calculate the length of each word in a list of strings.
#Answer:
words = ["Python", "Java", "HTML", "SQL"]
result = list(map(lambda word: len(word), words))

print(result)

#22.Given a list of integers, use filter() to select numbers greater than 50.

numbers = [20, 55, 40, 75, 90, 30, 60]

result = list(filter(lambda x: x > 50, numbers))

print(result)
#23. Use filter() with a lambda function to select numbers that are multiples of 4.
numbers = [4, 7, 8, 12, 15, 16, 20, 25]

result = list(filter(lambda x: x % 4 == 0, numbers))

print(result)

#Q24.Given a list of product prices, write a program to:
# Filter prices greater than ₹500
# Apply a 10% discount to the filtered prices using map()

prices = [250, 600, 800, 450, 1000, 1200]
filtered_prices = filter(lambda price: price > 500, prices)
discounted_prices = list(
    map(lambda price: price - (price * 10 / 100), filtered_prices)
)

print(discounted_prices)

#Q25.Given a list of integers, filter even numbers and then multiply each of them by 3 using a single pipeline.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(
    map(lambda x: x * 3,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)

#Q26.Given a list of numbers, filter numbers greater than 20 and then square each filtered number using map().
numbers = [10, 15, 25, 30, 18, 40]

result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x > 20, numbers))
)

print(result)
#Q27.Given a list of words, filter words whose length is greater than 4 and then convert those words into uppercase using a single pipeline.
words = ["cat", "apple", "banana", "dog", "python"]

result = list(
    map(str.upper,
        filter(lambda word: len(word) > 4, words))
)

print(result)

#Q28.Given a list of integers, filter numbers divisible by 5 and then add 10 to each of the filtered numbers.
numbers = [5, 12, 15, 20, 23, 30, 34]

result = list(
    map(lambda x: x + 10,
        filter(lambda x: x % 5 == 0, numbers))
)

print(result)

#Q29.Given a list of student marks, filter students who scored more than 40 and then increase their marks by 5 using map().
marks = [35, 45, 60, 30, 75, 40, 55]

result = list(
    map(lambda mark: mark + 5,
        filter(lambda mark: mark > 40, marks))
)

print(result)
#Q30. Given a list of strings, write a program using reduce() to concatenate all strings into a single string.

from functools import reduce

words = ["Python", "is", "easy"]

result = reduce(lambda x, y: x + y, words)

print(result)
#Q31.Given a list of digits, use reduce() to form a single number.
#Example: [1, 2, 3] → 123
from functools import reduce

digits = [1, 2, 3]

result = reduce(lambda x, y: x * 10 + y, digits)

print(result)
#Q32.Given a list of numbers, use reduce() to calculate the cumulative difference.
from functools import reduce

numbers = [100, 20, 10, 5]

result = reduce(lambda x, y: x - y, numbers)

print(result)

#Q33. Find total marks and average Given a list of student marks, use reduce() to find the total marks and then compute the average.
from functools import reduce

marks = [80, 75, 90, 85, 70]

total = reduce(lambda x, y: x + y, marks)

average = total / len(marks)

print("Total marks:", total)
print("Average:", average)

#Q34. Given a list of product prices, filter prices above ₹500, apply a 10% discount using map(), and compute the final total bill using reduce().

from functools import reduce

prices = [250, 600, 800, 450, 1000, 1200]

filtered = filter(lambda price: price > 500, prices)

discounted = map(lambda price: price * 0.90, filtered)

total = reduce(lambda x, y: x + y, discounted)

print("Final total bill:", total)

#Q35.Given a list of numbers, filter negative numbers, convert them into positive numbers using map(), and find their sum using reduce().

from functools import reduce

numbers = [10, -5, 20, -10, 30, -15]

negative = filter(lambda x: x < 0, numbers)

positive = map(lambda x: abs(x), negative)

total = reduce(lambda x, y: x + y, positive)

print("Sum:", total)

#Q36.Given a list of integers, filter numbers less than 50, multiply each by 3 using map(), and determine the maximum value using reduce().

from functools import reduce

numbers = [10, 25, 60, 15, 40, 75, 30]

filtered = filter(lambda x: x < 50, numbers)

multiplied = map(lambda x: x * 3, filtered)

maximum = reduce(lambda x, y: x if x > y else y, multiplied)

print("Maximum value:", maximum)

#Q37.Given a list of words, filter words with length greater than 3, convert them to uppercase using map(), and concatenate them into a single string using reduce().
from functools import reduce

words = ["cat", "apple", "dog", "python", "car", "java"]

filtered = filter(lambda word: len(word) > 3, words)

uppercase = map(lambda word: word.upper(), filtered)

result = reduce(lambda x, y: x + " " + y, uppercase)

print(result)

#Q38.A company tracks employee salaries. Filter salaries greater than ₹30,000, increase them by 15% using map(), and compute the total salary expenditure using reduce().

from functools import reduce

salaries = [25000, 35000, 40000, 28000, 50000]

filtered = filter(lambda salary: salary > 30000, salaries)

increased = map(lambda salary: salary * 1.15, filtered)

total = reduce(lambda x, y: x + y, increased)

print("Total salary expenditure:", total)

#Q39.A data analysis system stores a list of integers. Filter odd numbers, square each using map(), and compute their sum using reduce().
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]

odd_numbers = filter(lambda x: x % 2 != 0, numbers)

squared = map(lambda x: x ** 2, odd_numbers)

total = reduce(lambda x, y: x + y, squared)

print("Sum of squares:", total)

#Q40.An e-commerce platform stores product prices in a list. Filter products priced above ₹500, apply a 10% discount using map(), and calculate the total bill using reduce().

from functools import reduce

prices = [300, 600, 750, 450, 900, 1200]

filtered = filter(lambda price: price > 500, prices)

discounted = map(lambda price: price * 0.90, filtered)

total = reduce(lambda x, y: x + y, discounted)

print("Total bill:", total)

#Q41.A banking system stores transaction amounts. Filter only credit transactions (positive values), apply a processing bonus of ₹10 to each using map(), and calculate the total credited amount using reduce().

from functools import reduce

transactions = [1000, -500, 2000, -300, 1500]

credits = filter(lambda amount: amount > 0, transactions)

bonus = map(lambda amount: amount + 10, credits)

total = reduce(lambda x, y: x + y, bonus)

print("Total credited amount:", total)

#Q42.Given a list of integers, 
# filter numbers divisible by both 2 and 5,
#  add 5 to each using map(),
#  then find the product using reduce()
from functools import reduce
input_numbers = [10, 15, 20, 25, 30, 35, 40]
filtered_numbers = filter(lambda x: x % 2 == 0 and x % 5
    == 0, input_numbers)
result = reduce(lambda x, y: x * y, map(lambda x: x + 5, filtered_numbers))
print(result)