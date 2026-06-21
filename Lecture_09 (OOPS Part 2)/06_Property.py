# PROPERTY DECORATOR:- We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + " %"
    
s1 = Student(1, 2, 3)
print(s1.percentage)

s1.phy = 100
print(s1.percentage)