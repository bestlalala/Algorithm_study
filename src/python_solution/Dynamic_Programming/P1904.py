# 01타일
import sys
n = int(sys.stdin.readline())


def tiles(n):
    t = [0]*(n+1)
    t[1] = 1
    t[2] = 2
    for i in range(3, n+1):
        t[i] = (t[i-1] + t[i-2]) % 15746
    return t[n]


print(tiles(n))

