def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# testing the fib function
for num in range(21):
    print(fib(num))

'''
Скорость выполнения: O(Fibn), то есть полная хуета
А как надо?
'''


def fib_dynamic(n):
    fiblist = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fiblist[i] = fiblist[i-1] + fiblist[i-2]
    return fiblist[n]


# testing dynamic fib function
print(fib_dynamic(20))
