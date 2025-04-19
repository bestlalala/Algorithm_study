# 14501번. 퇴사

import sys
input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# dp[i] = i번째 날까지의 최대 수익
dp = [0] * (n+1)

for i in range(n):
    t, p = schedule[i]
    
    # 상담을 할 수 있다면
    if i + t <= n:
        dp[i + t] = max(dp[i+t], dp[i] + p)
    # 상담 안 하더라도 이전 수익을 유지
    dp[i + 1] = max(dp[i + 1], dp[i])


print(dp[n])