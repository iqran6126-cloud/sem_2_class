
def check(func):
    def wrapper(*args, **kwargs):
        print("Numbers are:", *args, **kwargs)
        result = func(*args, **kwargs)
        print("Result is:", result)
        print("-----------------")
        return result
    return wrapper




@check
def add(a, b):
    return a + b


@check
def subtract(a, b):
    return a - b


@check
def multiply(a, b):
    return a * b


@check
def divide(a, b):
    return a / b


add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
