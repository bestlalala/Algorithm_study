# 2606번. 바이러스

import sys
import collections
input = sys.stdin.readline

n = int(input().rstrip())   # 컴퓨터의 수
m = int(input().rstrip())   # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

coms = collections.defaultdict(set)
visited = collections.defaultdict(bool)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    coms[a].add(b)
    coms[b].add(a)

for i in range(n):
    visited[i+1] = False

def bfs(v):
    que = collections.deque([v])
    cnt = 0
    
    while que:
        v = que.popleft()
        cnt += 1
        visited[v] = True
        
        while coms[v]:
            c = coms[v].pop()
            if not visited[c] and c not in que:
                que.append(c)
                coms[c].remove(v)
    
    return cnt

print(bfs(1)-1)