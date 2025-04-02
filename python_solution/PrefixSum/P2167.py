# 2167번. 2차원 배열의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

ps = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        ps[i][j] = nums[i-1][j-1] + ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1]
   

k = int(input().rstrip())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # (i, j) ~ (x, y) 합 구하기
    print(ps[x][y] - ps[x][j-1] - ps[i-1][y] + ps[i-1][j-1])
    