import pytest
import allure


@pytest.allure.step
def test_DemoAllure():
    allure.MASTER_HELPER.attach("")
    print("Hello Allure reporting")