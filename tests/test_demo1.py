from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Any pytest file should start with test_ or end with _test
# When you run pytest command it will look for test_ files so we always start pytest file with test_

# Pytest standards will use functions only
#eg: These are called test Methods. Always start functions with test
import pytest
# Method name should have sense
# -k stands for method names execution(-k searches regular expression(here method name is our regular expresion),
# -s shows logs in output, -v stands for more info

'''
# How to Run them :
1. commands from command prompt
2. test runner available in pyCharm
If u run directly no o/p will be printed.
Use -s to print output. eg: py.test -v -s
-v => for more info.
py.test => running all test files in that specific folder path.
py.test <filename> => runs specific file.
py.test -k <methodname> => runs particular method or test.
You can mark (tag) tests @pytest.mark.smoke and then run with -m 

You can skip tests with @pytest.mark.skip
@pytest.mark.xfail => no o/p will be reported but method will get executed.

Fixtures are used as setup and teardown methods for test cases => 
conftest file to generalize fixtures and make it available to all TCs.

Data driven and parametarization can be done with return statements in tuple format
When U define fixture scope to class only, it will run once before class is initiated and at the end 

'''

def test_firstTC(setup):
    print("Hello iam using setup fixture in test_demo1 test\n")

def test_secondTC():
    print("Good Morning\n")

@pytest.mark.smoke
def test_selectedMethod():
    print("Running selectedMethod\n")
