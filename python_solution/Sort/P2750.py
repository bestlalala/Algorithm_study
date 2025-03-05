# 수 정렬하기
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))


def selection_sort(A):
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
    return None


selection_sort(A)
for i in range(n):
    print(A[i])

