# 23971번. ZOAC 4

import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().rstrip().split())

row = w // (m+1)
col = h // (n+1)

if w % (m+1) != 0:
    row += 1
if h % (n+1) != 0:
    col += 1

print(row*col)