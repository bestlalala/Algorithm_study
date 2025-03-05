# 10026번 적록색약
from collections import deque

n = int(input())
paint = [list(map(str, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if paint[nx][ny] == paint[x][y]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


ncw = 0 # 색약 아님
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ncw += 1
print(ncw, end=' ')

cw = 0  # 색약
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cw += 1
print(cw)






