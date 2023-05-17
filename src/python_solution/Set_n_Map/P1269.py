# 대칭 차집합

an, bn = map(int, input().split())
A = set(int(i) for i in input().split())
B = set(int(i) for i in input().split())

print(len((A-B)|(B-A)))

