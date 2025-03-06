# 1026번. 보물

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr_a = [int(i) for i in input().rstrip().split()]
arr_b = [int(i) for i in input().rstrip().split()]

s = 0
for i in range(n):
    a, b = min(arr_a), max(arr_b)
    s += a * b
    del arr_a[arr_a.index(a)]
    del arr_b[arr_b.index(b)]
print(s)