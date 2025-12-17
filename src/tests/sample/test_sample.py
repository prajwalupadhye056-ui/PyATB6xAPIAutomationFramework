import pytest
import allure

@allure.title("Verify Failed !! that the framework is working")
def test_sample_fail():
    assert True == False

@allure.title("Verify Passed !! that the framework is working")
def test_sample_pass():
    assert True == True