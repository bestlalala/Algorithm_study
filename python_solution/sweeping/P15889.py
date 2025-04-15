# 15889번. 호 안에 수류탄이야!!

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

flag = True
if n > 1:
    dist = list(map(int, input().split()))

    now = arr[0] + dist[0]
    for i in range(1, n-1):
        if now >= arr[i]:
            now = max(now, arr[i] + dist[i])

    if now < arr[-1]:
        flag = False

if flag:
    print("권병장님, 중대장님이 찾으십니다")
else:
    print("엄마 나 전역 늦어질 것 같아")
    