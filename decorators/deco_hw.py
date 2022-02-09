def deco(inner):
    def func():
        inner()
        print("Hello from decorator!")
    return func


@deco
def simple():
    print("Simple function")


simple()
