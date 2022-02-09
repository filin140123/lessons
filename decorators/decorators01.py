def deco(inner):
    def func(*args, **kwargs):
        inner()
        print(*args, *kwargs)

    return func


@deco
def simple(*args, **kwargs):
    print("Simple function")


simple("one", "two")
simple(one="one", two="two")
