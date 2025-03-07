# 20922번. 겹치는 건 싫어

import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이

s, e, cnt = 0, 0, 0
temp = collections.Counter()
max_len = 0

while e < n:
    if temp[arr[e]] < k:
        temp[arr[e]] += 1
        e += 1
        cnt += 1
    else:
        temp[arr[s]] -= 1
        s += 1
        cnt -= 1
    
    # print("s:", s, "e:", e, temp)
    max_len = max(max_len, cnt)
    
print(max_len)