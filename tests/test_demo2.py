import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = 'Hello test demo2'
    assert msg == 'Hi', "test failed bcoz Strings do not match"


def test_selectedMethod():
    print("Running selectedMethod in test_demo2")

def test_add():
    a = 5+6
    assert a==11, "Adding didnot match"
    print(a)
