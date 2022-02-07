def counter(x):
    count = 1
    while count <= x:
        yield count
        count += 1


c = counter(10)

for n in c:
    print(n)
