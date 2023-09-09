# 11000번. 강의실 배정
import heapq
import sys
input = sys.stdin.readline

n = int(input())
timetable = [[int(t) for t in input().split()] for _ in range(n)]

timetable.sort()

rooms = [0]
for s, e in timetable:
    if rooms[0] <= s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, e)

print(len(rooms))
