# OopsDemo is Parent Class

from OopsDemo import Calculator

class ChildImp(Calculator):  #Inherited Calculator class(parent class) into ChildImp class(child class)
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation() + self.sum

obj = ChildImp()
print(obj.getCompleteData)
