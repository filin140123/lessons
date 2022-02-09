def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x * x * x


# testing
for i in range(1, 8):
    print(product(i, square), end="\n" if i == 7 else " ")

for i in range(1, 8):
    print(product(i, cube), end="\n" if i == 7 else " ")
