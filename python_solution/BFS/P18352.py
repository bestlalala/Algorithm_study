# 18352번. 특정 거리의 도시 찾기

import sys
import collections
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    

def bfs(start):
    que = collections.deque([start])
    visited = [-1] * (n+1)
    visited[start] = 0
    
    answer = []
    
    while que:
        v = que.popleft()
        
        if visited[v] == k:
            answer.append(v)
        
        for i in graph[v]:
            if visited[i] == -1:
                que.append(i)
                visited[i] = visited[v] + 1
    
    return answer        
        
answer = bfs(x)

if answer:
    answer.sort()
    for a in sorted(answer):
        print(a)
else:
    print(-1)
    