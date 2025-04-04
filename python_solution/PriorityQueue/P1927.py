# 1927번. 최소 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
heapq.heapify(arr)

for _ in range(n):
    x = int(input())
    
    # x가 자연수: 배열에 x 추가
    if x > 0:
        heapq.heappush(arr, x)        
    # x가 0: 배열에서 가장 작은 값 출력하고 그 값을 배열에서 제거
    elif x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            # 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0 출력
            print(0)
