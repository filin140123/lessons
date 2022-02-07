def even_odd():
    count = 1
    while True:
        if count % 2 == 0:
            yield "even"
        else:
            yield "odd"
        count += 1


x = even_odd()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
