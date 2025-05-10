# 2805번. 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

original_total = sum(tree)

low, high = 1, max(tree)
answer = 0

while low <= high:
    mid = (low + high) // 2
    
    total = sum(min(mid, t) for t in tree)
    get = original_total - total
    
    if get >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)