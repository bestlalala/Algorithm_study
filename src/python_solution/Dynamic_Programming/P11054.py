# 11054번. 가장 긴 바이토닉 부분 수열


n = int(input())
A = [int(m) for m in input().split()]

up = [1] * n
down = [1] * n

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            up[i] = max(up[i], up[j] + 1)
        if A[n-1-j] < A[n-1-i]:
            down[n-1-i] = max(down[n-1-i], down[n-1-j] + 1)

for i in range(n):
    up[i] = up[i] + down[i]

print(max(up) - 1)

