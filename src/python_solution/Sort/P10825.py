# 10825번. 국영수

n = int(input())
scoreboard = [[i for i in input().split()] for _ in range(n)]

scoreboard.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in scoreboard:
    print(s[0])
