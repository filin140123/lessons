def create_patterns(max_patterns=100):
    patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
    i = 0
    resultlist = []
    while len(resultlist) < max_patterns:
        if i >= len(patterns):
            i = 0
        resultlist.append(patterns[i])
        i += 1
    return resultlist


def get_current_pattern():
    patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1


c = get_current_pattern()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))