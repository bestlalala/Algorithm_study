# 2559번. 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

ps = [0] * (n+1)

for i in range(1, n+1):
    ps[i] = ps[i-1] + nums[i-1]

# print(ps)

max_value = -float('inf')   # 구간합이 0 이하일 수도 있음!

for i in range(k, n+1):
    max_value = max(max_value, ps[i] - ps[i-k])

print(max_value)