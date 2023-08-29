# 2848번. 피보나치 수 2
# n번째 피보나치 수 출력하기


def fibonacci(num):
    f = [0, 1, 1]
    if num >= len(f):
        for i in range(len(f), num + 1):
            f.append(f[i-1] + f[i-2])
    print(f[num])


n = int(input())
fibonacci(n)
