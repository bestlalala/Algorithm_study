# 파도반 수열
import sys
t = int(sys.stdin.readline())


def pado(n):
    if n <= 10:
        p = [0] * 11
    else:
        p = [0] * (n+1)
    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2
    p[5] = 2
    p[6] = 3
    p[7] = 4
    p[8] = 5
    p[9] = 7
    p[10] = 9
    for i in range(11, n+1):
        p[i] = p[i-5] + p[i-1]
    return p[n]


for _ in range(t):
    n = int(sys.stdin.readline())
    print(pado(n))

