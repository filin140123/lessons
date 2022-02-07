import time


def get_number_from_range():
    for n in range(10):
        yield n


c = (n for n in range(10))
print(c, " = ", sum(c))
d = [n for n in range(10)]
print(d, " = ", sum(d))
e = list(range(10))
print(e, " = ", sum(e))

list_start_time = time.time()
print(sum([n for n in range(1000000)]))
list_process_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum(n for n in range(1000000)))
gen_process_time = time.time() - gen_start_time

print(f'Processing time list is {list_process_time}')
print(f'Processing time generator is {gen_process_time}')
