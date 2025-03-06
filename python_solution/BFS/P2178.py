# 2178번. 미로 탐색

import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
mymap = [[int(i) for i in input().rstrip()] for _ in range(n)]

# 상하좌우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    que = collections.deque([(r, c)])
    
    while que:
        r, c = que.popleft()  # 현재 위치 및 이동 거리
         
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and mymap[nr][nc] == 1:
                mymap[nr][nc] = mymap[r][c] + 1     # 거리 계산
                que.append((nr, nc))
    
    return mymap[n-1][m-1]

print(bfs(0, 0))