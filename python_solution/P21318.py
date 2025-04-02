# 21318번. 피아노 체조

import sys
input = sys.stdin.readline

n = int(input().rstrip())
hard = list(map(int, input().split()))
q = int(input().rstrip())
question = [ list(map(int, input().split())) for _ in range(q)]

# x번부터 y번까지 몇 개의 악보에서 실수하게 될지

arr = [0] * n
for i in range(0, n-1):
    if i > 0:
        arr[i] += arr[i-1]
    if hard[i] > hard[i+1]:
        arr[i] += 1

arr[n-1] = arr[n-2]
# print(arr)

for x, y in question:
    # x부터 y까지 합
    if x == y:
        print(0)
    elif x == 1:
        print(arr[y-2])
    else:
        print(arr[y-2] - arr[x-2])
