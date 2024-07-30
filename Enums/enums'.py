from enum import Enum


class Locatorenums(Enum):
    get_Started_Button = "Get started"


class Sample:
    print(f"{Locatorenums['get_Started_Button'].value}")
