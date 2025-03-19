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

# 다른 풀이
# n = int(input())
# points = [tuple(int(p) for p in input().split()) for _ in range(n)]

# points.sort()

# length = 0
# last_start = points[0][0]
# last_end = points[0][1]
# for x, y in points[1:]:
#     # 완전히 새로운 선분
#     if last_end < x:
#         length += last_end - last_start
#         last_start = x
#     last_end = max(last_end, y)
# length += last_end - last_start

# print(length)