# 14502번. 연구소

import sys
from itertools import combinations
from collections import deque
# import copy

input = sys.stdin.readline

# 벽 세우기
# 바이러스 퍼뜨리기
# 안전영역 계산하기

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(lab, n, m):
    que = deque()
    # temp_lab = copy.deepcopy(lab)
    temp_lab = [row[:] for row in lab]  # deepcopy 대신 얕은 복사 활용 (속도 더 빠름)
    
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 2:
                que.append((i, j))
    
    while que:
        r, c = que.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and temp_lab[nr][nc] == 0:
                temp_lab[nr][nc] = 2    # 바이러스 퍼뜨리기
                que.append((nr, nc))
        
    # 안전 영역 계산하기 (0의 개수 세기)
    safe_area = sum(row.count(0) for row in temp_lab)
    return safe_area

# 입력 받기
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세울 수 있는 모든 위치 찾기
empty_space = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]

max_safe_area = 0

# 3개의 벽을 세울 수 있는 모든 조합을 탐색
for walls in combinations(empty_space, 3):
    # 벽 세우기
    for r, c in walls:
        lab[r][c] = 1
    
    # 바이러스 퍼뜨리기
    safe_area = bfs(lab, n, m)
    max_safe_area = max(max_safe_area, safe_area)
    
    # 벽을 다시 허물기 (원상복구)
    for r, c in walls:
        lab[r][c] = 0
    
print(max_safe_area)