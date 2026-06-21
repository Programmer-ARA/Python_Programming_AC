# 'PRIVATE(like) ATTRIBUTES & METHODS':-
#       Private attributes & methods are meant to be used only within the class and are not accesible from outside of the class.

class Account:
    __name = "Anonymouos" # Private Class Attributes

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private Object Attributes

    def reset_pass(self):
        print(self.__acc_pass)  # Not show error breacouse the attribute is within the class

    def __hello(self):    # Private Methods
        print("Hello")
    
        
a1 = Account("12345", "abc")

print(a1.acc_no)
print(a1.__acc_pass)    # Not printed (Throws Error)
a1.reset_pass()