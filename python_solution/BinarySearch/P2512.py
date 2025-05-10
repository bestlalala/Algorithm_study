# 2512번. 예산

import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().split()))
m = int(input())

sum_request = sum(request)
if sum_request <= m:
    print(max(request))
else:
    low = 0
    high = max(request)
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2
        total = sum(min(r, mid) for r in request)
        
        if total <= m:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(answer)