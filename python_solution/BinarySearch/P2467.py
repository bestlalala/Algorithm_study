# 2467번. 용액 
# - 이진탐색 풀이 (투포인터가 더 효율적)

n = int(input())
values = list(map(int, input().split()))

ans = float('inf')
ans_left, ans_right = 0, 0

for i in range(n-1):
    cur = values[i]
    
    low, high = i+1, n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        tmp = cur + values[mid]
        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        
        if tmp < 0:
            low = mid + 1
        else:
            high = mid - 1

print(values[ans_left], values[ans_right])
