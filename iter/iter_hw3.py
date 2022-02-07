def infinite_square_generator():
    count = 1
    while True:
        yield count ** 2
        count += 1


isg = infinite_square_generator()
print(next(isg))
print(next(isg))
print(next(isg))
print(next(isg))
