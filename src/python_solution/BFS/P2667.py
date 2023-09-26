# 2667번: 단지번호 붙이기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0 # 방문한 점은 0으로 만들어서 다시 방문하지 않게
    cnt = 1

    while que:
        x, y = que.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0   # 방문한 것으로 표시
                que.append((nx, ny))
                cnt += 1
    return cnt

# 1인 지점부터 찾아서 시작
cnt_list = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            cnt_list.append(bfs(matrix, i, j))

cnt_list.sort()
print(len(cnt_list))    # 총 단지수
for c in cnt_list:
    print(c)
