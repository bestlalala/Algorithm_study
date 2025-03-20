# 11725번. 트리의 부모 찾기

import sys
import collections
input = sys.stdin.readline

n = int(input().rstrip())

graph = collections.defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    

# 부모 노드 정보를 저장할 배열
parent = [0] * (n+1)   
visited = [0] * (n+1)    # 방문 여부 저장

def bfs(node):
    que = collections.deque()
    que.append(node)
    
    while que:
        now = que.pop()
        visited[now] = 1
        
        for i in graph[now]:
            if visited[i]:
                parent[now] = i
            else:
                que.append(i)

bfs(1)
for i in range(2, n+1):
    print(parent[i])