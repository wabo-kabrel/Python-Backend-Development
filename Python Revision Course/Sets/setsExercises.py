#1. Program to find common elements in two lists using sets
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
s1=set(l1)
s2=set(l2)

commons = s1 & s2   #Or s1.intersection(s2)
commonList = list(commons)
print(commonList)


#2. Program to check if a set is a subset of another
s1={1,2,3,4,5}
s2={4,5}
if s2.issubset(s1):
   print ("s2 is a subset of s1")
else:
   print ("s2 is not a subset of s1")