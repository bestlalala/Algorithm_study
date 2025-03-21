# 15654번. N과 M(5)

import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
for arr in permutations(nums, m):
    print(' '.join(map(str, arr)))
