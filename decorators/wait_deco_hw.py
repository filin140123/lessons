from functools import wraps
from time import sleep


def wait(value):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(value)
            print(f"There was a pause {value} seconds before execution {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return inner


@wait(5)
def print_hi():
    print("Hi!")


print_hi()
