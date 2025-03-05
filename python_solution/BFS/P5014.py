# 5014 스타트링크
import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = set()
cnt = [0] * (F+1)


def bfs(v):
    que = deque()
    que.append(v)
    visited.add(v)

    while que:
        v = que.popleft()
        if v == G:
            return cnt[G]
        for nv in (v+U, v-D):
            if nv not in visited and 1 <= nv <= F:
                visited.add(nv)
                cnt[nv] = cnt[v] + 1
                que.append(nv)
    if cnt[G] == 0:
        return "use the stairs"


print(bfs(S))
