# A unicode string is a sequence of code points, which are numbers from 0 through
#0x10FFFF (1,114,111 decimal). This sequence of coding needs to be represented in memory as
#a set of code units, and code units are then mapped to 8-bit bytes.

# Character Encoding
# The rules for translating a Unicode string into a sequence of bytes are called a character encoding.
# Three types of encodings are present, UTF-8, UTF-16 and UTF-32. UTF stands for Unicode Transformation Format.
# Python 3.0 onwards has built-in support for Unicode. The str type contains Unicode characters, 
# hence any string created using single, double or the triple-quoted string syntax is stored as Unicode.
# The default encoding for Python source code is UTF-8.

# Example:
var = "3/4"
print (var)
var = "\u00BE"  # Unicode character of 3/4
print (var)     # Output: 3/4

var = "\u0031\u0030"    # Unicode character of 10
print (var)             # Output: 10.

# Strings display the text in a human-readable format, and bytes store the characters as binary data. 
#Encoding converts data from a character string to a series of bytes. Decoding translates the bytes 
#back to human-readable characters and symbols. It is important not to confuse these two methods. 
#Encode is a string method, while decode is a method of the Python byte object.

#Example: We have a string variable below that consists of ASCII characters. ASCII is a subset
#of Unicode character set. The encode() method is used to convert it into a bytes object.

string = "Hello"
to_bytes = string.encode('utf-8')
print (to_bytes)                        # Result: b'Hello'
string = to_bytes.decode('utf-8')       # Back to string
print (string)                          # Result: Hello
