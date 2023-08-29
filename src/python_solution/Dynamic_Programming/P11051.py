# 11051번. 이항 계수 2

n, k = map(int, input().split())

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(n+1):
    for j in range(n+1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)
