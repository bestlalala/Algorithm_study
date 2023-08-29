# 11053번. 가장 긴 증가하는 부분 수열

n = int(input())
A = [int(m) for m in input().split()]

dp = [1]*n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
