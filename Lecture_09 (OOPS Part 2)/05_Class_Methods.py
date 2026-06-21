# "class" METHODS:- A class method is bound to the class & receives the class as an implicit first argument.
# NOTE:- static methods can't access or modify class state & generally for utility.

class Person:
    name = "Anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name
    
    # # Without using class decorator
    # def change_name(self, name):
    #     self.__class__.name = name


p1 = Person()
p1.change_name("Rahul Gandhu")
print(p1.name)
print(Person.name)