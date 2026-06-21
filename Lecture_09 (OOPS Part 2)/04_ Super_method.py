# 'super' METHODS:- super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stoped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # super Method

c1 = ToyotaCar("Fortuner", "Electric")
print(c1.type)
