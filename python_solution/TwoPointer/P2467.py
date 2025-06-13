# 2467번. 용액 - 투포인터

n = int(input())
values = list(map(int, input().split()))

# 이분탐색: 더했을 때 0에 가장 가까운 두 용액 찾기
left, right = 0, n-1

ans = abs(values[left] + values[right])
ans_left = left
ans_right = right

while left < right:
    tmp = values[left] + values[right]
    if abs(tmp) < ans:
        ans = abs(tmp)
        ans_left = left
        ans_right = right

        if ans == 0:
            break
    
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(values[ans_left], values[ans_right])