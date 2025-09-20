# File handling in Python lets you:
# - Open files.
# - Read data from files.
# - Write data to files.
# - Close files after usage.


# Basic File Operations
# - Open a file                 open()
# - Read from a file            .read(), .readline(), .readlines()
# - Write to a file             .write(), .writelines()
# - Close a file                .close()
 
 
# File Modes
# When opening a file, you must specify the mode:
# - 'r'             Read (default). Error if file doesn't exist
# - 'w'             Write. Creates files or overwrites.
# - 'a'             Append. Adds to end of file.
# - 'x'             Create a new file. Error if file already exists.
# - 'b'             Binary mode (e.g. 'rb', 'wb').
# - 't'             Text mode (default, e.g. 'rt').

# Ex1: Reading a File
file = open("sample.txt", "r")      # Opens sample.txt in read mode.
content = file.read()               # Reads the content and stores it in content.
print(content)                      # Prints the content.
file.close()                        # Closes file.

# Ex2: Writing to a File
file = open("newfile.txt", "w")
file.write("Hello, world!")
file.close()
# - If newfile.txt doesn't exist, it is created.
# - If it exists, its content is replaced.


# Ex3: Appending to a File
file = open("newfile.txt", "a")
file.write("\nThis is a new line.")
file.close()
#  Adds text to the end of the file without deleting existing content.


# Using 'with' Statement (Recommended)
# This is the safest and cleanest way to handle files:
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)



# Advantages
# - Automatically closes the file after the block.
# - Cleaner syntax. 


# Reading Line-by-Line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())


# Common Methods
# - .read(size)	            Reads size characters
# - .readline()	            Reads one line
# - .readlines()	        Reads all lines as a list
# - .write(string)	        Writes a string to the file
# - .writelines(list)	    Writes a list of strings to the file
# - .close()	            Closes the file


# Ex4: Reading Lines into a List
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# Handling Files That Don't Exist
# You can use try-except blocks to avoid crashes
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")



# Summary:
# - Use open() to work with files.
# - Use 'r', 'w', 'a' modes to control file behavior.
# - Always close the file (or use with for auto-closing).
# - Use .read(), .write(), etc. for reading/writing.

