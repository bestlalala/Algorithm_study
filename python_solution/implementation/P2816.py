# 2816번. 디지털 티비

import sys
input = sys.stdin.readline

n = int(input().rstrip())
channel = [input().rstrip() for _ in range(n)]

idx1, idx2 = channel.index('KBS1'), channel.index('KBS2')

result = '1'*idx1 + '4'*idx1

if idx1 < idx2:
    result += '1'*idx2 + '4'*(idx2-1)
else:
    result += '1'*(idx2+1) + '4'*idx2

print(result)