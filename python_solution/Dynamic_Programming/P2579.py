# 계단 오르기

n = int(input())
s = [int(input()) for _ in range(n)]

dp = []
if n > 2:
    dp = [s[0], max(s[0] + s[1], s[1]), max(s[0] + s[2], s[1] + s[2])]
    for i in range(3, n):
        dp.append(max(dp[i-2] + s[i], dp[i-3]+s[i]+s[i-1]))
    print(dp[-1])
else:
    if n == 1:
        print(s[0])
    else:
        print(s[0] + s[1])



