# 좌표 정렬하기 2

n = int(input())

pos = [tuple(int(m) for m in input().split()[:2]) for _ in range(n)]

pos.sort(key=lambda x: (x[1], x[0]))

for i in pos:
    print(i[0], i[1])

