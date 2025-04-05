#1. Find the number of vowels in a given string:

my_string = "All animals are equal. Some animals are more equal"
vowels = "aeiou"
count = 0

for x in my_string:
    if x.lower() in vowels:
        count += 1
print (f"There are {count} vowels in my_string")


#2. Convert a string with binary digits to integer

myString = '10101'

def strToInt(myString):
   for x in myString:
      if x not in '01': return "Error. String with non-binary characters"   # If any character is not '0' or 
                                                                            #'1',   it returns an error.
   num = int(myString, 2)       # This uses Python's built-in int() function to convert from base 2 to base 10.
   return num
print ("binary:{} integer: {}".format(myString,strToInt(myString)))