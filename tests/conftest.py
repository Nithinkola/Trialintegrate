import pytest

# this is Generic way of using fixtures. Where ever setup is passed as parameter in method,
# it looks for that setup method fixture in that file if not available looks for conftest file fixtures.
@pytest.fixture()
def setup():
    print("\tI will execute first")
    yield
    print("\tI will execute last")

@pytest.fixture(scope="class")
def dummy_data():
    num1 = 10
    num2 = 20
    print("Executing fixture setUp")
    #return [num1,num2]
    yield
    print("tearDown of fixture")

@pytest.fixture(scope="class")
def dataLoad():
    print("User profile data is created.")
    return["Rahul", "Shetty", "rahulshettyacademy@gmil.com"]

