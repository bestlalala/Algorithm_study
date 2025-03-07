# 11659번. 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cases = [list(map(int, input().split())) for _ in range(m)]

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + nums[i-1]

for i, j in cases:
    print(dp[j]-dp[i-1])

