# 좌표 정렬하기

n = int(input())

pos = [tuple(int(m) for m in input().split()[:2]) for _ in range(n)]

pos.sort()

for p in pos:
    print(p[0], p[1])