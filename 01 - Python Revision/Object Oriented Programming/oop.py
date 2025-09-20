# Object-Oriented Programming (OOP) is a programming paradigm based on
#the concept of objects. These objects contain:
# - Data (attributes/properties)
# - Behavior (methods/functions)
# It's like modeling real-world things in code.


# Why Use OOP?
# - Code reusability (via inheritance).
# - Easier maintenance.
# - Better structure and modularity.
# - Encapsulation of data.


# 04 Pillars of OOP in Python
#1. Encapsulation: Bind data and methods together, hide details.
#2. Abstraction: Show only necessary features, hide complexity.
#3. Inheritance: Reuse code from existing classes.
#4. Polymorphism: One interface, many forms (method overriding or overloading).


# Basic Terminology
# - Class:          Blueprint for creating objects.
# - Object:         An instance of a class.
# - Method:         Function defined inside a class.
# - Attribute:      Variable that belongs to a class or object.
# - self:           Refers to the current instance of the class.
# - Constructor:    __init__() method for initializing objects.


# - Defining a Class and Object
class Person:                                       # The object here is Person
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# - Creating an object
p1 = Person("John", 21)
p1.greet()                  # Output: Hello, my name is John and I'm 21 years old.


# - Inheritance
# Allows a class (child) to inherit attributes and methods from another class (parent):
class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"My name is {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying Python")

s1 = Student("John")
s1.intro()
s1.study()


# - Encapsulation 
# Hide internal details underscore _ or double underscore __
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500


# - Polymorphism
# Different classes, same method name — handled differently:
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())


# - Class vs Instance Variables
class MyClass:
    class_var = 0  # Shared by all instances

    def __init__(self, value):
        self.instance_var = value  # Unique to each instance


# Special (Magic) Methods
# Python classes have built-in dunder (double underscore) methods.


# Ex2:

class Car:              # The class name should always begin with a capital letter

    def __init__(self, make, model, year, color):     # This __init__ method constructs objects for us.
        self.make = make        # assigning the make attribute of self to the make argument.      
        self.model = model            
        self.year = year             
        self.color = color            


    def drive (self):           # drive(self) is a method and self refers to the object 
                                #that's using the method.
        print("This car is driving")

    def stop(self):
        print("This car is stopped")
