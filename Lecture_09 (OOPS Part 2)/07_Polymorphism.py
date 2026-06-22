# POLYMORPHISM: Operator Overloading
# When the same operator is allowed to have different meaning according to the context.
# Example:-

# print(1 + 3) # 4
# print("Golu" + " Bhaiya")    # Concatenate
# print([1, 2, 3] + [4, 5, 6])    # Merge

# Here "+" is used diffrently in each print function (Operator Overloading)
# Called implicit overloading.


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(3,4)
num1.showNumber()

num2 = Complex(5,7)
num2.showNumber()

sum = num1 + num2
sum.showNumber()

sub = num2 - num1
sub.showNumber()

# sum = num1.add(num2)
# sum.showNumber()


