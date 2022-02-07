number_list = [1, 2, 3, 4, 5]

for n in number_list:
    print(n)

for letter in "string":
    print(letter)

nl_iter = iter(number_list)
print(type(nl_iter))
str_iter = iter("string")
print(type(str_iter))

# print(nl_iter.__next__())
# print(nl_iter.__next__())
# print(nl_iter.__next__())
# print(nl_iter.__next__())
# print(nl_iter.__next__())
#
# print(next(nl_iter))
# print(next(nl_iter))
# print(next(nl_iter))
# print(next(nl_iter))
# print(next(nl_iter))


def iter_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print("Iteration stopped")
            break


iter_for_loop(number_list)
iter_for_loop("hello")
