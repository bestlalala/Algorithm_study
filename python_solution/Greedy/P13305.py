# 13305번. 주유소

import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))

min_price = float('inf')
res = 0
for i in range(n-1):
    if city[i] < min_price:
        min_price = city[i]
    res += min_price * dist[i]

print(res)