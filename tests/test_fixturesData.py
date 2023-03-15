# using fixtures passing data into methods.

import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class Testexample2(BaseClass):
    def test_editprofile(self, dataLoad):
        print(dataLoad)
        log = self.getLogger()    # we are able to access getLogger() method of BaseClass.
        log.info(dataLoad[0])
        print(dataLoad[0])
        print(dataLoad[2])
