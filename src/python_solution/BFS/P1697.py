# 1697번 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    que = deque()
    que.append(v)

    while que:
        v = que.popleft()
        if v == k:
            return dist[v]
        for nv in (v-1, v+1, v*2):
            if 0 <= nv <= MAX and not dist[nv]:
                dist[nv] = dist[v] + 1
                que.append(nv)


MAX = 100000
dist = [0] * (MAX+1)

n, k = map(int, input().split())
print(bfs(n))
