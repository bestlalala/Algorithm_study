# 1966번. 프린터 큐

import sys
import collections
input = sys.stdin.readline

tn = int(input())
for _ in range(tn):
    n, m = map(int, input().split())
    star = list((map(int, input().split())))
    
    que = collections.deque()
    for i in range(n):
        que.append((star[i], i))
    
    cnt = 0
    while que:
        priority, idx = que.popleft()
        flag = False
        for i in range(len(que)):
            if que[i][0] > priority:
                flag = True
                break
        if flag:
            que.append((priority, idx))
        else:
            cnt += 1
            if idx == m:
                break
    
    print(cnt)