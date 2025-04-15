# 11723번. 집합

import sys
input = sys.stdin.readline

m = int(input())

S = 0

for _ in range(m):
    parts = input().split()
    c = parts[0]
    x = 0
    
    if len(parts) > 1:
        x = int(parts[1])
    if c == 'add':
        S |= (1 << x)
    elif c == 'remove':
        S &= ~(1 << x)
    elif c == 'check':
        if (S & (1 << x)) != 0:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        S ^= (1 << x)
    elif c == 'all':
        S = (1 << 21) - 1   # 1~20번까지 켠다.
    elif c == 'empty':
        S = 0
