# INHERITANCE:- When one class(child/derived) derives the properties & methods of another class(parent/base).

# Types of INHERITANCE:--

# 1.    'SINGLE INHERITANCE':- Single Child/Derived and single parent/Base Class.
# Example:-

class car:  # Parent/Base
    @staticmethod
    def start():
        print("Car Started")

    def stop():
        print("Car Stoped")

class ToyotaCar(car):   # Child/Derived
    def __init__(self, name):
        self.name = name

c1 = ToyotaCar("Fortuner")
c2 = ToyotaCar("prius")

print(c1.name)
c1.start()  # Inherited property due to inheritance


# 2.    'MULTI-LEVEL INHERITANCE':- Multilevel inheritance occurs when a derived class becomes the base class for another class, allowing properties and methods to be inherited through multiple levels.
# Example:-

class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj = Child()

obj.show_grandparent()
obj.show_parent()
obj.show_child()



# 3.    'MULTIPLE INHERITANCE': In this the child/derived class inherit the property from the multiple Parent/Base Class

class A:
    varA = "welcomr to class A"

class B:
    varB = "welcomr to class B"

class C(A, B):
    varC = "welcomr to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)




