# 1715번. 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = [int(input().rstrip()) for _ in range(n)]

heapq.heapify(card)

cnt = 0

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    cnt += a + b

print(cnt)