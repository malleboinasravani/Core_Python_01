#Q1. Assign the built-in function len to a variable called count. Use it to find the length of a list.
count = len

numbers = [10, 20, 30, 40, 50]

print(count(numbers))
#Q2. Write a function run_twice(func, value) that calls func on value twice and returns the final result.
def run_twice(func, value):
    first = func(value)
    second = func(first)
    return second


print(run_twice(lambda x: x * 2, 5))
#Q3. Store the functions upper, lower, and title in a dictionary. Let the user choose which one to apply.
operations = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}

text = input("Enter a string: ")
choice = input("Choose upper, lower, or title: ")

result = operations[choice](text)

print(result)
#Q4. Write a function that returns another function.
#make_multiplier(3) should return a function that multiplies any number by 3.
def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


multiply_by_3 = make_multiplier(3)

print(multiply_by_3(5))
print(multiply_by_3(10))
#Q5. Can you store the same function under multiple names in a dictionary?

def greet(name):
    return "Hello " + name


functions = {
    "first": greet,
    "second": greet,
    "third": greet
}

print(functions["first"]("Sravani"))
print(functions["second"]("Sravani"))
print(functions["third"]("Sravani"))
