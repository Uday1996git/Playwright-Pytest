import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://playwright.dev/python")


@pytest.fixture()
def get_url(request):
    url = request.config.getoption("--url")
    return url
