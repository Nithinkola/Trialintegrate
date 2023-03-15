import pytest


@pytest.mark.usefixtures("dummy_data")
class TestCalculatorClass:
    def test_distance(self):
        print("Test distance function")
        #assert self.distance(self.num1, self.num2) == 10

    def test_sum_of_square(self):
        print("Test sum of square function")
        #assert self.sum_of_square(self.num1, self.num2) == 500

    def test_distanceAgain(self):
        print("Test distance function second time")
        #assert self.distance(self.num1, self.num2) == 10

    def test_sum_of_squareAgain(self):
        print("Test sum of square function second time")
        # assert self.sum_of_square(self.num1, self.num2) == 500


'''
def distance(num1, num2):
    return abs(num1 - num2)

def sum_of_square(num1, num2):
    return num1 ** 2 + num2 ** 2
'''
