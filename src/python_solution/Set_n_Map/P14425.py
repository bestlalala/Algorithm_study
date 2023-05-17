# 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

S = set([input() for _ in range(n)])

cnt = 0
for _ in range(m):
    i =input()
    if i in S:
        cnt += 1

print(cnt)