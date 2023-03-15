class Calculator:
    num = 100 #Class Variable. (Variables defined inside Class are called Class Variables)

    # default constructor.
    def __init__(self):  #Instance variables. (Variables defined inside Constructor are called Instance Variables)
        print("Iam called automatically when object is Created.")

    def getData(self):
        print("Iam a method in a class")

obj = Calculator() # Syntax to create Object in Python
obj.getData()
n = obj.num
print(n)
