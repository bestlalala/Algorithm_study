# 2606번. 바이러스

import sys
import collections
input = sys.stdin.readline

n = int(input().rstrip())   # 컴퓨터의 수
m = int(input().rstrip())   # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

coms = collections.defaultdict(list)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    coms[a].add(b)
    coms[b].add(a)

def bfs(v):
    que = collections.deque([v])
    visited[v] = True   # 방문 표시
    cnt = 0
    
    while que:
        v = que.popleft()

        for c in coms[v]:
            if not visited[c]:
                que.append(c)
                visited[c] = True
                cnt += 1    # 감염된 컴퓨터 수 증가
    
    return cnt

print(bfs(1))