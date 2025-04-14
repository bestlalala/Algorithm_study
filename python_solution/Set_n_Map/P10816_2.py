# 10816번. 숫자 카드 2

import sys
import collections
input = sys.stdin.readline

n = int(input())
card = collections.Counter(list(map(int, input().split())))

m = int(input())
nums = list(map(int, input().split()))

res = []
for num in nums:
    res.append(card[num])

print(' '.join(map(str, res)))
