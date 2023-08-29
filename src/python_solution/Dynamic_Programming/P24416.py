# 알고리즘 수업 - 피보나치 수 1

fib_cnt = 1
fibonacci_cnt = 0


def fib(n):
    global fib_cnt
    if n == 1 or n == 2:
        return 1
    else:
        fib_cnt += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global fibonacci_cnt
    f = [None] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        fibonacci_cnt += 1
    return f[n]


n = int(input())
fib(n)
fibonacci(n)
print(fib_cnt, fibonacci_cnt)

