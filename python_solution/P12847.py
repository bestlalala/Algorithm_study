# 12847번. 꿀 아르바이트

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

# 연속 m일 근무 -> 최대값

window = sum(t[:m])
max_money = window

for i in range(m, n):
    window += t[i] - t[i-m]
    max_money = max(max_money, window)
    
print(max_money)