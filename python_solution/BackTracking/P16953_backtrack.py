# 16953번. A -> B

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

min_result = float('inf')

def backtrack(n, cnt):
    global min_result
    
    if n == b:
        min_result = min(min_result, cnt)
        return
    elif n < b:
        backtrack(n*2, cnt + 1)
        backtrack(n*10 + 1, cnt + 1)

backtrack(a, 0)

if min_result == float('inf'):
    print(-1)
else:
    print(min_result + 1)