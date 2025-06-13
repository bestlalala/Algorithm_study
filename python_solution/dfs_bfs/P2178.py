# 2178번. 미로 탐색

import collections

n, m = map(int, input().split())
graph = [[int(i) for i in input()] for _ in range(n)]

def bfs(sr, sc):
    que = collections.deque([(sr, sc)])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while que:
        r, c = que.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                    que.append((nr, nc))
                    graph[nr][nc] = graph[r][c] + 1

    return graph[n-1][m-1]

print(bfs(0, 0))
        