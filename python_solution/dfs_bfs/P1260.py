# 1260번. DFS와 BFS
import collections

n, m, v = map(int, input().split())

# 오름차순 정렬이 필요하므로 인접리스트 사용
graph = [[] for _ in range(n+1)]

for _ in range(m):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

# 정렬
for i in graph:
    i.sort()

visited = [False] * (n+1)

def dfs(graph, start, visited):
    visited[start] = True  # 현재 노드 방문 처리
    print(start, end = ' ')
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    visited = [False] * (n+1)
    que = collections.deque([start])
    visited[start] = True
    
    while que:
        v = que.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


# DFS로 탐색한 결과
dfs(graph, v, visited)

print()

# BFS로 탐색한 결과
bfs(graph, v)


