# 10610번. 30

import sys
input = sys.stdin.readline
n = list(input().rstrip())


if '0' not in n:
    print(-1)
elif sum(map(int, n)) % 3 != 0:
    print(-1)
        
else:
    n.sort(reverse=True)
    print(''.join(n))