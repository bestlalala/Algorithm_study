# 11728번. 배열 합치기

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

# 두 배열 정렬하면서 합치기
def merge(n, m, A, B):
    arr = []
    a, b = 0, 0
    while a < n or b < m:
        if a == n:  # A 배열을 다 쓴 경우
            arr.extend(B[b:])
            break
        if b == m:  # B 배열을 다 쓴 경우
            arr.extend(A[a:])
            break
        if A[a] < B[b]:
            arr.append(A[a])
            a += 1
        else:
            arr.append(B[b])
            b += 1
    return arr

print(' '.join(map(str, merge(n, m, arr_A, arr_B))))