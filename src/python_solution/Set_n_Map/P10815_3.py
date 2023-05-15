import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
checks = [int(n) for n in input().split()]

for check in checks:
    low, high = 0, n-1  # cards의 이진 탐색 index
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > check:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif cards[mid] < check:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')