# 1052번. 물병

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 1 개수
def numOf1(n):
    return bin(n).count('1')

cnt = 0
while numOf1(n) > k:
    # 맨 오른쪽에 있는 1 
    buy = n & -n
    n += buy
    cnt += buy 

print(cnt)