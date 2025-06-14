# 1931번. 회의실 배정

n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])
# print(meetings)

result = []
last = 0
for m in meetings:
    if last <= m[0]:
        result.append(m)
        last = m[1]

# print(result)
print(len(result))