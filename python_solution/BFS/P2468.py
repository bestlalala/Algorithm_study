# 2468번 안전영역
from collections import deque

n = int(input())
city = [[int(c) for c in input().split()] for _ in range(n)]

# 기준 높이 k: max(city)부터 -1

# k보다 높은 곳들만 bfs 돌면서 안전 영역 개수 세기

# 안전 영역의 수 저장해 놓고, 그 중 최댓값 출력
maxNum = 0
for i in range(n):
    maxNum = max(city[i])

safe_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, k):
    que = deque()
    que.append((x, y))
    visited.add((x, y))

    while que:
        x, y = que.popleft()
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if (nx, ny) not in visited and city[x][y] >= k:
                que.append((nx, ny))
                visited.add((nx, ny))


for k in range(maxNum):
    visited = set()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if city[i][j] > k and (i, j) not in visited:
                bfs(i, j, k+1)
                cnt += 1

    if safe_area < cnt:
        safe_area = cnt

print(safe_area)