class Calculator:
    num = 100  # Class Variable. (Variables defined inside Class are called Class Variables)

    # default constructor.
    def __init__(self, a, b):  # Instance variables. (Variables defined inside Constructor are called Instance Variables)
        self.firstNum = a
        self.secondNum = b
        print("Iam called automatically when object is Created.")

    def summation(self):
        sum = self.firstNum + self.secondNum + Calculator.num
        return sum

    def getData(self):
        print("Iam a method in a class")

# Syntax to create Object in Python
obj = Calculator(2, 3)
print(obj.summation())
obj.getData()
n = obj.num
print(n)
