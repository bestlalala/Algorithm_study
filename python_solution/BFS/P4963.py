# 4963번. 섬의 개수

import sys
from collections import deque
input = sys.stdin.readline


dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(graph, w, h, sr, sc, visited):
    que = deque()
    que.append((sr, sc))
    visited[sr][sc] = True
    
    while que:
        r, c = que.popleft()
        
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and graph[nr][nc] == 1:
                    que.append((nr, nc))
                    visited[nr][nc] = True  # 방문 표시
    return


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 1 and not visited[r][c]:
                bfs(graph, w, h, r, c, visited)
                cnt += 1
    print(cnt)
