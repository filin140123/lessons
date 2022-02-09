from functools import wraps


def prohibit_kw(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("Keyword arguments are not allowed")
        return func(*args, **kwargs)
    return wrapper


def prohibit_int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if type(value) is int:
                raise ValueError("Integer arguments are not allowed")
        for value in kwargs.values():
            if type(value) is int:
                raise ValueError("Integer arguments are not allowed")
        return func(*args, **kwargs)
    return wrapper


@prohibit_kw
def print_hello(name):
    print(f"Hello {name}!")


@prohibit_int_args
def print_numbers(*args, **kwargs):
    print(*args, *kwargs)


# Working
print_hello("James")
print_numbers(1.0, 2.0, 3.0)

# Not working
print_hello(name="James")
print_numbers(1, 2, 3)
