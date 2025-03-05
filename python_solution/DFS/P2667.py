# 2667번. 단지번호붙이기
import sys
input = sys.stdin.readline

N = int(input().rstrip())

mymap = [[int(i) for i in input().rstrip()] for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(r, c, cnt):
    visited[r][c] = True   # 방문 처리
    cnt += 1   
    
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and mymap[ny][nx] == 1:
            cnt = dfs(ny, nx, cnt)
            
    return cnt

cnt_list = []
for i in range(N):
    for j in range(N):
        if mymap[i][j] == 1 and not visited[i][j]:
            cnt_list.append(dfs(i, j, 0))

cnt_list.sort()
print(len(cnt_list))
for c in cnt_list:
    print(c)