# 5549번. 행성 탐사

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())

mymap = [input().rstrip() for _ in range(m)]

dp = [[[0] * 3 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j][0] - dp[i-1][j-1][0]
        dp[i][j][1] = dp[i][j-1][1] + dp[i-1][j][1] - dp[i-1][j-1][1]
        dp[i][j][2] = dp[i][j-1][2] + dp[i-1][j][2] - dp[i-1][j-1][2]
        if mymap[i-1][j-1] == 'J':
            dp[i][j][0] += 1
        elif mymap[i-1][j-1] == 'O':
            dp[i][j][1] += 1
        elif mymap[i-1][j-1] == 'I':
            dp[i][j][2] += 1
        
# print(dp)

for _ in range(k):
    a, b, c, d = map(int, input().split())
    res = [0] * 3
    res[0] = dp[c][d][0] - dp[c][b-1][0] - dp[a-1][d][0] + dp[a-1][b-1][0]
    res[1] = dp[c][d][1] - dp[c][b-1][1] - dp[a-1][d][1] + dp[a-1][b-1][1]
    res[2] = dp[c][d][2] - dp[c][b-1][2] - dp[a-1][d][2] + dp[a-1][b-1][2]
    
    # print(res)
    print(' '.join(map(str, res)))