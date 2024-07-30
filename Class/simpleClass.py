class A:

    def __init__(self, value):
        print("This is a constructor")
        self.value = value
        return

    def print_value(self):
        print(self.value)
        return

    def welcome(self):
        print("Welcome to my first Class")
        return

    def second_Function(self):
        print("Second Function")
        return

    def args(self, a, b):
        return a * b


if __name__ == 'main':
    obj = A("Hello")
    obj.welcome()
    obj.second_Function()
    print(obj.args(20, 30))
    obj1 = A("Hello")
    obj1.print_value()
