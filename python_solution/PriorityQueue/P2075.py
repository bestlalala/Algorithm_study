# 2075번. N번째 큰 수

import sys
import heapq
input = sys.stdin.readline

n = int(input())

nums = []
min_value = float('inf')
for _ in range(n):
    for i in list(map(int, input().split())):
        # print(i, min_value)
        if len(nums) < n:
            heapq.heappush(nums, i)
        else:
            if i > nums[0]:
                heapq.heappop(nums)
                heapq.heappush(nums, i)

print(heapq.heappop(nums))