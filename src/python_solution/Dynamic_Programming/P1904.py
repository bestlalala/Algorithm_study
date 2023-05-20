# 01타일
n = int(input())

def factorial(nf):
    f = [None]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, nf+1):
        f[i] = i * f[i-1]
    return f[nf]


# def combination(n, r):
#     if r == 1:
#         return n
#     elif r > n/2:
#         return combination(n, n-r)
#     factorial(n)/factorial(r)
#     nCr = factorial(n)/(factorial(r)*factorial(n-r))
#     return nCr


def tiles(n):
    t = [0]*(n+1)
    t[1] = 1
    t[2] = 2
    for i in range(3, n+1):
        for j in range(0, n/2):   # j: 00의 개수
            o = n-j*2   # o: 1의 개수
            if j == 0:
                t[i] += 1
            elif j == 1:
                t[i] += o+1
            else:
                t[i] += factorial(j+o)/(factorial(j)*factorial(o))
    return t[n]


print(factorial(n))
print(tiles(n))

