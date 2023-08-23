# 11055번. 가장 큰 증가하는 부분 수열

n = int(input())
A = [int(m) for m in input().split()]

dp = [0] * n
dp[0] = A[0]

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])
        else:
            dp[i] = max(dp[i], A[i])

print(max(dp))
