# 7562번 나이트의 이동
from collections import deque
import sys

input = sys.stdin.readline

# dr dc 설정확실하게 하자!!
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(y, x, gr, gc):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        r, c = queue.popleft()

        if r == gr and c == gc:  # 방문하고자 하는 곳이면
            print(visited[r][c] - 1)
            return

        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]

            if (0 <= rr < l) and (0 <= cc < l) and not visited[rr][cc]:
                queue.append([rr, cc])
                visited[rr][cc] = visited[r][c] + 1


t = int(input())
for _ in range(t):
    l = int(input())
    nr, nc = map(int, input().split())
    gr, gc = map(int, input().split())

    if nr == gr and nc == gc:
        print(0)
        continue

    visited = [[False] * l for _ in range(l)]
    bfs(nr, nc, gr, gc)
