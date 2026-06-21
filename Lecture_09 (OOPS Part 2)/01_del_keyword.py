# 'del' KEYWORD:- Used to delete object properties or object itself.

class Student:
    def __init__(self, name):
        self.name = self.name

s1 = Student("Abdur")
del s1
print(s1) #error beacouse the object is deleted.
