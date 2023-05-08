# 세 수
# 세 정수 중 두 번째로 큰 정수 출력

A = [int(n) for n in input().split()]
n = len(A)


for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if A[j] < A[min]:
            min = j
    A[i], A[min] = A[min], A[i]

print(A[1])

