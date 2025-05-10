# 1654번. 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

low, high = 1, max(lan)
answer = 0

while low <= high:
    mid = (low + high) // 2
    

    total = 0
    for l in lan:
        total += l // mid
    
    if total < n:
        high = mid - 1
    else:
        answer = mid
        low = mid + 1

print(answer)