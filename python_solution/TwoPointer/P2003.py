# 2003번. 수들의 합2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s, e, cnt, temp = 0, 0, 0, 0

while e < n:
    temp += nums[e]     # e번째 값 추가
    e += 1              # e 한칸 이동
    
    # 현재 부분합(temp)이 m보다 크거나 같으면 s를 이동
    while temp > m and s < e:
        temp -= nums[s]  # s번째 값을 빼고
        s += 1  # s 한칸 이동
    
    if temp == m:
        cnt += 1
    
print(cnt)