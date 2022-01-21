from random import sample

input()  # input data from user
print()  # output data to user

# read data from file old way
text = open("sample.txt")
for line in text:
    print(line, end="")
text.close()

# read data from file convienient way
with open("sample.txt", "r") as text:
    for line in text:
        print(line, end="")

# read data from file with while loop
with open("sample.txt", "r") as text:
    line = text.readline()
    while line:
        print(line, end="")
        line = text.readline()

print("\n---")

# read data from file as list of lines
with open("sample.txt", "r") as text:
    lines = text.readlines()
print(lines)

# read data from file as is
with open("sample.txt", "r") as text:
    full = text.read()
print(full)
