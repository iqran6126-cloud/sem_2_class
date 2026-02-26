def deco(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

def say_hi():
    print("Hi!")

say_hi = deco(say_hi)
say_hi()
