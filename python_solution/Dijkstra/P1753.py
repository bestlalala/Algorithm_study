# 1753번. 최단경로
import heapq

INF = float('inf')

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]    # 인접리스트
distance = [INF] * (V+1)            # v번 노드까지의 최단 거리

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # u->v 가중치 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 가는 경우가 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
                
