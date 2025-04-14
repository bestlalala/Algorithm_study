# 10815번. 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
card = set(list(map(int, input().split())))

m = int(input())
nums = list(map(int, input().split()))

res = ''
for num in nums:
    if num in card:
        res += '1'
    else:
        res += '0'

print(' '.join(res))
