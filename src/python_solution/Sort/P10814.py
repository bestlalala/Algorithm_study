# 나이순 정렬

n = int(input())

judge_list = [[m for m in input().split()[:2]] for _ in range(n)]

for i in judge_list:
    i[0] = int(i[0])

judge_list.sort(key=lambda x: (x[0]))

for i in judge_list:
    print(i[0], i[1])