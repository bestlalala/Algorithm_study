# 15652번. N과 M(4)

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

res = []

def backtrack(res):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(1, n+1):
            if len(res) == 0 or i >= res[-1]:
                res.append(i)
                backtrack(res)
                res.pop()

backtrack(res)