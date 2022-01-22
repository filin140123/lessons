x = 127
pow(10, 3)  # 1000
pow(x, 0)  # 1

print(x == pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))  # True

for i in range(1, 10):
    print(str(bin(i))[2:])

y = 0b110
print(y)

z = 0x11
print(z)

print(hex(1024))
print(0x10, 0x20, 0x40, 0x80, 0x100, 0x200, 0x400)
