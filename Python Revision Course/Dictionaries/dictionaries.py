# A dictionary is a collection of key-value pairs. It allows you to 
#store, retrieve, and update data using a key, rather than a numeric
#index (like lists).

# Syntax:

my_dict = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}


# Features
# - Keys are unique and immutable. You can only delete them entirely, but 
#you can't change (changing its identity/name) them once created.
# - Values are mutable.
# - Values can be of any data type.
# - Access elements via keys.
# - Dynamic (grows as you add data).


# Accessing and Modifying Dictionary Items
# - Access a value
print(my_dict["name"])  # Output: Alice

# - Add or Update a key
my_dict["age"] = 26  # Updates value
my_dict["country"] = "Cameroon"  # Adds new key

# - Delete a key
del my_dict["job"]

# - Loop through keys
for key in my_dict:
    print(key)

# - Loop through values
for value in my_dict.values():
    print(value)

# - Loop through key-value pairs
for key, value in my_dict.items():
    print(f"{key} → {value}")



# Common Dictionary Methods
# - .get(key, default):     	Safely get a value
# - .keys():                	Returns all keys
# - .values():         	Returns all values
# - .items():          	Returns key-value pairs
# - .update():         	Adds/updates another dictionary
# - .pop(key):         	Removes and returns the value of a key
# - .clear():       	Removes all items


# Nested Dictionaries
# You can store a dictionary in another dictionary!
students = {
    "001": {"name": "Alice", "grade": "A"},
    "002": {"name": "Bob", "grade": "B"}
}
print(students["001"]["name"])  # Output: Alice


# Use Cases
# - Storing user profiles.
# - Fast data lookup.
# - Counting items.
# - Representing structured data (like JSON).

# NB:
# - Keys must be immutable (e.g. strings, numbers, tuples).
# - Mutable types like lists can't be used as keys.
{["name"]: "Alice"}  # ❌ Error: list is unhashable
# - Duplicate keys are not allowed. The last value will overwrite previous ones.


profile = {
    "username": "kabrel",
    "skills": ["Python", "HTML", "Cloud"],
    "active": True
}

print(profile.get("skills"))  # ['Python', 'HTML', 'Cloud']


