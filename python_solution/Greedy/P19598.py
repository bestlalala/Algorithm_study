# 19598번. 최소 회의실 개수

import sys
import heapq
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

room = []

meeting.sort()

for s, e in meeting:
    if room and room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room, e)

print(len(room))
