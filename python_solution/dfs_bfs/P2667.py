# 2667번. 단지번호 붙이기

import collections

n = int(input())

graph = [[int(i) for i in input()] for _ in range(n)]

def bfs(sr, sc):
    que = collections.deque([(sr, sc)])
    visited = [[False] * n for _ in range(n)]
    visited[sr][sc] = True
    graph[sr][sc] = 0
    cnt = 1
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    que.append((nr, nc))
                    visited[nr][nc] = True
                    graph[nr][nc] = 0
                    cnt += 1
    
    return cnt

danji = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            danji.append(bfs(i, j))

danji.sort()

print(len(danji))
for dan in danji:
    print(dan)

    