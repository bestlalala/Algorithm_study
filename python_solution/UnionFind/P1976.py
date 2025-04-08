# 1976번. 여행 가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

parent = list(range(n+1))

# 특정 원소의 루트 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n): 
        if city[i][j] == 1:
            union(i+1, j+1)

root = find(plan[0])
result = all(find(city) == root for city in plan)

print("YES" if result else "NO")
