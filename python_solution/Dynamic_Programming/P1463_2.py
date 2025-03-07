# 1463번. 1로 만들기

import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * 1000001

for i in range(4, n+1):
    dp[i] = dp[i-1]
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]) 
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])

    dp[i] += 1

print(dp[n])
