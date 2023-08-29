# 14002번. 가장 긴 증가하는 부분 수열 4

n = int(input())
A = [int(m) for m in input().split()]

dp = [1] * n
B = list()

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
max_len = max(dp)
print(max_len)

for i in range(n-1, -1, -1):
    if dp[i] == max_len:
        B.append(A[i])
        max_len -= 1

B.reverse()

for i in range(len(B)):
    print(B[i], end=" ")
