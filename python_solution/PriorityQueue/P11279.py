# 11279번. 최대 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())
    
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)    

