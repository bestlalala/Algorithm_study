# 2109번. 순회강연

import sys
import heapq
input = sys.stdin.readline

n = int(input())
dmax = -1

lec = []

for _ in range(n):
    p, d = map(int, input().split())
    if d > dmax:
        dmax = d
    heapq.heappush(lec, (-d, -p))

cnt = 0
pq = []

# day 기준 내림차순 정렬
# day 이하 p 내림차순 정렬
for day in range(dmax, 0, -1):
    while lec and day == -lec[0][0]:
        d, p = heapq.heappop(lec)
        heapq.heappush(pq, p)
    
    if pq:
        cnt -= heapq.heappop(pq)    # 매일 일정 -> 그리디

print(cnt)
