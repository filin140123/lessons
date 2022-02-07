number = input("Enter the number: ")

try:  # trying to run the code
    print(int(number) / 2)
except TypeError:  # error handling
    print("You have to enter a number...")
else:  # if code runs successfully, executing else-block
    print("Else block")
finally:  # finally-block runs in any case, even if "break" was called
    print("Finally")


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except TypeError:
        print("x and y must be numbers")


print(divide(4, 2))
print(divide(4, 0))
print(divide(4, "s"))
