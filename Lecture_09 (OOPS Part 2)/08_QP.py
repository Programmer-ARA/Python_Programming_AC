# # # ----------- QUESTION - 01 -----------
# # Define a circle class to create a circle with radius r using the constructor. Define Area() method of the class which calculates the area of the cicle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the cicle.

# class Cicle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return (22/7) * self.r ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.r
    
# c1= Cicle(21)
# print(c1.area())
# print(c1.perimeter())


# # # ----------- QUESTION - 02 -----------
# # Define a Employee class with attributes role, department, & salary. This class also has a showDetail() method. Then create an Engineer class that inherits from employee & has additional attributes: name & age.

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
    
#     def showDetails(self):
#         print("Role: ", self.role, "\nDepartment: ", self.department, "\nSalary: ", self.salary)
    
# # E1 = Employee("Accountant", "Finance", "50000")

# # E1.showDetails()

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Developer", "IT Department", "60000")

# Eng1 = Engineer("Abdur", "19")
# Eng1.showDetails() 


# # ----------- QUESTION - 03 -----------
# Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that: order1 > order2 if price order1 > if price order2


class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    
ord1 = Order("Chips", 20)
ord3 = Order("Tea", 10)

print(ord1 > ord3)

