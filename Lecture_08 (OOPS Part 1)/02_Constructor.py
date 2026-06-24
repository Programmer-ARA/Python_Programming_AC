# __init__ function or Constructor:-
# All classes have a function called __init__() which is always executed when the object is being initiated.

# There are two types of Constructor:-
# 1. Default Contructor:
#       def __init__(self):
#          pass

# 2. Parameterized Constructor:-
# def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in the database.....")



# creating class

class Student:
    def __init__(self, name, marks):
        # The "'self" parameter is a reference to the current instance of the class, 
        # and is used to access variables that belongs to the class.
        self.name = name
        self.marks = marks
        print("Adding new student in the database.....")

s1 = Student("Abdur", 97)
print(s1.name)
print(s1.marks)

s2 = Student("Arjun", 87)
print(s2.name)
print(s2.marks)

