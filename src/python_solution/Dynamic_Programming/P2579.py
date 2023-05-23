# 계단 오르기

n = int(input())

s = []
for _ in range(n):
    s.append(int(input()))

dp = [s[0], max(s[0] + s[1], s[1]), max(s[0] + s[2], s[1] + s[2])]
for i in range(3, n):
    dp.append(max(dp[i-2] + s[i], dp[i-3]+s[i]+s[i-1]))

print(dp[-1])


