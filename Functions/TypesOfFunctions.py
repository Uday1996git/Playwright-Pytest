def noArgs():
    print("Welcome")
    return


def sumFN(a, b):
    c = a + b
    print(str(c))
    return


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def display(a, b, c):
    return add(multiply(a, b), c)


print(display(4, 20, 10))
