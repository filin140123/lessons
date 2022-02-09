def print_function_data(function):
    """
    This is decorator function that prints the function data
    :param function:
    :return:
    """
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation: {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def square_sum(a, b):
    """
    :param a: first number
    :param b: second number
    :return: sum of squares of two numbers
    """
    return a * a + b * b


print(square_sum(2, 3))
print(square_sum.__doc__)
print(square_sum.__name__)
help(square_sum)
