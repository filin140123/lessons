from time import time
from functools import wraps

# start_time = time.time()
# sum([number for number in range(1000000)])
# print(time.time() - start_time)
#
# start_time = time.time()
# sum(number for number in range(1000000))
# print(time.time() - start_time)


def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Code execution time: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(1_000_000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(1_000_000))


@speed_test
def product(range_value=1_000_00):
    result = 1
    for number in range(1, range_value):
        result *= number
    return result


sum_with_list()
sum_with_gen()
product()
