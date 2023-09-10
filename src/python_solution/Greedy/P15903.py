# 15903번. 카드 합체 놀이
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = [int(a) for a in input().split()]

heapq.heapify(cards)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    temp = x + y
    heapq.heappush(cards, temp)
    heapq.heappush(cards, temp)

print(sum(cards))
