# 1926번. 그림
from collections import deque

n, m = map(int, input().split())
graph = [[int(d) for d in input().split()] for _ in range(n)]

# 하, 상, 우, 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    que = deque()
    que.append((a, b))
    graph[a][b] = 0
    cnt = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 더이상 이동할 곳이 없는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1
    return cnt


paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))


