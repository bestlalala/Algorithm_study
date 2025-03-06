# 2606번. 바이러스

n = int(input())
m = int(input())

adj = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

global cnt
cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1


def dfs(v):
    visited[v] = 1
    global cnt
    for i in range(n+1):
        if visited[i] == 0 and adj[v][i] == 1:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
