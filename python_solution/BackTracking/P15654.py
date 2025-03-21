# 15654번. N과 M(5)

import sys
# from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# nums.sort()
# for arr in permutations(nums, m):
#     print(' '.join(map(str, arr)))

def backtrack(arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    else:
        for num in nums:
            if num not in arr:
                arr.append(num)
                backtrack(arr)
                arr.pop()
          
nums.sort()      
backtrack([])