# 2156번. 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input().rstrip()) for _ in range(n)]

# dp[i] = k
# i번째 잔까지 있을 때 마실 수 있는 최대 포도주의 양

dp = [-1] * 10001

if n == 1:
    dp[1] = wine[0]
elif n == 2:
    dp[2] = wine[0] + wine[1]
elif n == 3:
    dp[3] = max(wine[0] + wine[1], wine[1] + wine[2], wine[2] + wine[0])
else:
    dp[1] = wine[0]
    dp[2] = wine[0] + wine[1]
    dp[3] = max(wine[0] + wine[1], wine[1] + wine[2], wine[2] + wine[0])
    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i-1], dp[i-3] + wine[i-2] + wine[i-1])
        
print(dp[n])