# 2589번 보물섬
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
myMap = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif myMap[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1


result = 0
for i in range(n):
    for j in range(m):
        if myMap[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
