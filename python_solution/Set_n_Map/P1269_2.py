# 1269번. 대칭 차집합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res1 = A - B
res2 = B - A

print(len(res1) + len(res2))