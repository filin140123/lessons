with open("binary_data", "bw") as b:
    b.write(bytes(range(21)))

with open("binary_data", "br") as b:
    for i in b:
        print(i)
