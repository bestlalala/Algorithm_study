# 2206번. 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

mymap = [[int(i) for i in input().rstrip()] for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

min_dist = float('inf')

# 방문 배열: visited[row][col][break_wall]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    
    que = deque([(0, 0, 1, 0)]) # (r, c, 거리, 벽을 부쉈는지 여부)
    visited[0][0][0] = True
    

    while que:
        r, c, dist, broken = que.popleft()
        
        if r == n-1 and c == m-1:
            return dist
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < n  and 0 <= nc < m:
                # 이동할 수 있는 길인 경우
                if mymap[nr][nc] == 0 and not visited[nr][nc][broken]:
                    visited[nr][nc][broken] = True
                    que.append((nr, nc, dist+1, broken))
                
                # 벽이지만 부수고 이동할 수 있는 경우
                if mymap[nr][nc] == 1 and broken == 0 and not visited[nr][nc][1]:
                    visited[nr][nc][1] = True
                    que.append((nr, nc, dist+1, 1))

    return -1


print(bfs())