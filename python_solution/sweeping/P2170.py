# 2170번. 선 긋기

import sys
input = sys.stdin.readline

n = int(input().rstrip())

line = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    line.append((a, 1))
    line.append((b, -1))
    
line.sort(key=(lambda x: x[0]))

length = 0 # 선의 길이
k = 0   # 중첩된 선의 수
for i in range(2*n-1):
    k += line[i][1]
    if k >= 1:
        length += line[i+1][0] - line[i][0]

print(length)