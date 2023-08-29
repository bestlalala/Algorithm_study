# 1010번. 다리 놓기

C = [[-1 for _ in range(31)] for _ in range(31)]


def bino_coef(r, k):
    if C[r][k] == -1:
        for i in range(r+1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1] + C[i-1][j]
    print(C[r][k])


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    bino_coef(m, n)

