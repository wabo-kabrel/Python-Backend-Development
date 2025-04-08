#1. JSON File Handling
# JSON (JavaScript Object Notation) is a lightweight format for data
#exchange. Python has a built-in module called json.

# - Reading a JSON File
import json

# Read JSON data from a file
with open("data.json", "r") as file:
    data = json.load(file)          # json.load(file) converts JSON file to a Python dictionary or list.
    print(data)

# Example data.json content:
    {
    "name": "Kabrel",
    "age": 19,
    "skills": ["Python", "Cloud", "Web Dev"]
    }

# - Writing to a JSON File
import json

info = {
    "name": "Kabrel",
    "age": 19,
    "skills": ["Python", "Cloud", "Web Dev"]
}

# Save dictionary as JSON
with open("output.json", "w") as file:
    json.dump(info, file, indent=4)

# json.dump() writes the Python dict to the file.
# indent = 4 makes it nicely formatted.


#2. CSV File Handling
# CSV (Comma-Separated Values) is often used in spreadsheets and databases.
# Python has a built-in csv module.
# - Reading a CSV file
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)               # Reads the file line-by-line
    for row in reader:
        print(row)                      # Each row is a list of strings

# Ex students.csv
'''
Name,Age,Skill
Kabrel,19,Python
Alex,19,Java
'''

# - Writing to a CSV file
import csv

with open("new_students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Skill"])
    writer.writerow(["Kabrel", 19, "Python"])
    writer.writerow(["Alex", 19, "Java"])


# - Reading CSV as Dictionaries
# You can read rows as dictionaries for better readability
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], "-", row["Skill"])



# Format	Module	    Functions
# JSON	    json	    load(), dump()
# CSV	    csv	        reader(), writer(), DictReader()


