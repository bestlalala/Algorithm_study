# 7569번. 토마토
from collections import deque
import sys
input=sys.stdin.readline

m, n, h = map(int, input().split())

# 1: 익은 토마토
# 0: 익지 않은 토마토
# -1: 토마토가 들어 있지 않은 칸

# 다 익으려면 최소 며칠?

que = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0


def bfs(graph):

    while que:
        # 높이, x, y tnstj
        z, x, y = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h):
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    que.append((nz, nx, ny))



boxes = []
for _ in range(h):
    boxes.append([[int(t) for t in input().split()] for _ in range(n)])

for a in range(h):
    for b in range(n):
        for c in range(m):
            if boxes[a][b][c] == 1:
                que.append((a, b, c))

bfs(boxes)

day = 0
for a in range(h):
    for b in range(n):
        for c in range(m):
            if boxes[a][b][c] == 0:
                print(-1)
                exit(0)
            day = max(day, boxes[a][b][c])
print(day-1)
