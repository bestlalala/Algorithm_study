# 7576번. 토마토
from collections import deque

m, n = map(int, input().split())
box = [[int(b) for b in input().split()] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    queue.append((nx, ny))

bfs()
for i in box:
    for j in i:
        # 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))

# 처음 시작을 1로 표현했으므로 1을 빼준다.
print(result - 1)
