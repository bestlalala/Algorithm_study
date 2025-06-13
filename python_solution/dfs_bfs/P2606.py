# 2606번. 바이러스

import collections

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(start):
    que = collections.deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 0
    
    while que:
        com = que.popleft()
        
        for i in network[com]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    
    return cnt

print(bfs(1))