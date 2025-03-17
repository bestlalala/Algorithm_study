# 15651번. N과 M

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
res = []

# 백트래킹
def backtrack(res):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(1, n+1):
            res.append(i)
            backtrack(res)
            res.pop()
            
backtrack(res)