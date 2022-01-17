# Map, Filter and Lambda Expressions

def sum_of_two(x):
    return x+x


numberlist = [1, 2, 3, 4, 5, 6, 7]

result = list(map(sum_of_two, numberlist))
print(result)

print(list(map(lambda n: n**3, numberlist)))
print(list(filter(lambda n: n % 2 == 1, numberlist)))
print(list(filter(lambda n: n % 2 == 0, numberlist)))
