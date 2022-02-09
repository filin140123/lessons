from functools import wraps


def check_if_first_arg_is(value):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f"First argument has to be {value}")
            return func(*args, **kwargs)
        return wrapper
    return inner


@check_if_first_arg_is('blue')
def print_rainbow_colors(*colors):
    print(colors)


print_rainbow_colors('red', 'yellow', 'green')
