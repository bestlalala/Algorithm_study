# 14503번. 로봇 청소기
from collections import deque

# 북 동 남 서 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [[int(i) for i in input().split()] for _ in range(n)]
visited = [[0]*m for _ in range(n)]

visited[r][c] = 1
cnt = 0


def bfs(r, c, d):
    global cnt
    queue = deque()
    queue.append((r, c)) # 로봇 위치
    visited[r][c] = 1
    cnt += 1

    while queue:
        x, y = queue.popleft()
        flag = 0

        for _ in range(4): # 반시계 방향으로 돌려감
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not area[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    flag = 1 # 반시계 방향으로 돌아갔을 때 빈칸이 있다는 것을 의미
                    break


        if flag == 0: # 청소할 곳이 없다면 후진
            if area[x - dx[d]][y - dy[d]] != 1:
                queue.append((x - dx[d], y - dy[d]))

            else:
                print(cnt)
                break

bfs(r, c, d)
