# 2644번. 촌수계산

n = int(input())
a, b = map(int, input().split())
m = int(input())    # 부모 자식들 간의 관계의 개수

family = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())    # 부모, 자식
    family[x].append(y)
    family[y].append(x)

visited = [False] * (n+1)

def dfs(v, cnt):
    visited[v] = True
    
    if v == b:
        return cnt
    
    for i in family[v]:
        if not visited[i]:
            res = dfs(i, cnt+1)
            if res != -1:
                return res

    return -1

print(dfs(a, 0))
