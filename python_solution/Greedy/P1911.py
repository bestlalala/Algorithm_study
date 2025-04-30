# 1911번. 흙길 보수하기

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
ungdungi = [list(map(int, input().split())) for _ in range(n)]

ungdungi.sort(key=lambda x: x[0])

now = 0
result = 0
for start, end in ungdungi:
    if now < start:
        now = start
    if now < end:
        board = (end - now + l -1) // l  # 필요한 널빤지 수
        result += board
        now += board * l    # 덮은 위치 걩신

print(result)