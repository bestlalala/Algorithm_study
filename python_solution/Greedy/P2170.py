# 2170번. 선 긋기
import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(int(p) for p in input().split()) for _ in range(n)]

points.sort()

length = 0
last_start = points[0][0]
last_end = points[0][1]
for x, y in points[1:]:
    # 완전히 새로운 선분
    if last_end < x:
        length += last_end - last_start
        last_start = x
    last_end = max(last_end, y)
length += last_end - last_start

print(length)
