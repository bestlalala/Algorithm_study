# 11722번. 가장 긴 감소하는 부분 수열

n = int(input())
A = [int(m) for m in input().split()]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if A[n-1-j] < A[n-1-i]:
            dp[n-1-i] = max(dp[n-1-i], dp[n-1-j]+1)

print(max(dp))
