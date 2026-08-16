#Create a list containing dictionaries.
#  Perform a shallow copy and a deep copy. 
# Modify a value inside one dictionary in the 
# original list and display all lists.

import copy

original = [
    {"name": "Sravani", "age": 23},
    {"name": "Anu", "age": 22}
]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0]["age"] = 25

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)