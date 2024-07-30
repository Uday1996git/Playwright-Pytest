import logging
import time

import pytest
import os


# @pytest.fixture
# def testPytest_Ini(pytestconfig):
#     return pytestconfig.getoption('env')['url']


def test_pytest_Ini(get_url):
    logging.info("Before capturing the url value")
    # url = os.environ.get('url')
    url = get_url
    logging.info("After capturing the url value " + url)
    print("Hello url is " + url)
