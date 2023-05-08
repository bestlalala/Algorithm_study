# 수 정렬하기2

## sorted 사용
import sys
input=sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

for i in sorted(A):
    print(i)

