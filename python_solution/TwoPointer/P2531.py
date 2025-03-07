# 2531번. 회전 초밥

import sys
import collections
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

sushi.extend(sushi[:k-1])

s, e= 0, k

temp = collections.Counter(sushi[0:k])
max_cnt = len(temp) + (1 if c not in temp else 0)  # 쿠폰 초밥 고려

while s < n-1:
    temp[sushi[e]] += 1
    if temp[sushi[s]] == 1:
        del temp[sushi[s]]
    else:
        temp[sushi[s]] -= 1
    e += 1
    s += 1
    
    if c not in temp:
        max_cnt = max(max_cnt, len(temp)+1)
    else:
        max_cnt = max(max_cnt, len(temp))
        
print(max_cnt)