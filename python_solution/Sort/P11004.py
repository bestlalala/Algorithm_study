# 11004번. k번째 수

n, k = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()
print(A[k-1])
