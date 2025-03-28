# 2285번. 초콜릿 식사

import sys
input = sys.stdin.readline

k = int(input())

lowbit, cnt = k & -k, 0
while lowbit < k:
    lowbit <<= 1
    cnt += 1

print(lowbit, cnt)
