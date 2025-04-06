#1. Program to create a new dictionary by extracting
#the keys from a given dictionary.

d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2={}
for k in keys:
   d2[k]=d1[k]
print (d2)

#2. Program to convert a dictionary to a list of (k,v) tuples
d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
L1 = list(d1.items())
print (L1)

#3. Program to remove keys with the same values in a dictionary
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())#all values
uvals = [v for v in vals if vals.count(v)==1]#unique values
d2 = {}
for k,v in d1.items():
   if v in uvals:
      d = {k:v}
      d2.update(d)
print ("dict with unique value:",d2)        # Output: dict with unique value: {'three': 3, 'four': 44}