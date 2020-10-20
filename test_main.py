from selenium import webdriver
# import pytest
import time
from TestBase import TestBase
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_run():
    mf = TestBase()
    # try:
    #     mf.test_login()
    # except False:
    #     sys.exit()
    mf.test_login()
    mf.test_loc_task()
    mf.test_loc_project()
    mf.test_loc_case()
    mf.test_execute()


if __name__ == '__main__':
    # pytest.main()
    test_run()
    # time.sleep(5)
