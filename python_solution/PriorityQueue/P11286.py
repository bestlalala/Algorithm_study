# 11286번. 절대값 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    x = int(input())
    
    if x:
        if x < 0:
            heapq.heappush(nums, (-x, 0))
        else:
            heapq.heappush(nums, (x, 1))
    elif x == 0:
        # 절대값이 가장 작은 값 빼내서 출력
        if nums:
            x, i = heapq.heappop(nums)
            # print(x, i)
            if i:
                print(x)
            else:
                print(-x)
        else:
            print(0)