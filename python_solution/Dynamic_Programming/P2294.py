# 2294번. 동전 2

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [100001] * (k+1)
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
