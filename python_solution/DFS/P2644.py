# 2644번. 촌수계산

n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식들간의 관계의 개수

myGraph = dict()
visited = set()
result = set()

for i in range(m):
    x, y = map(int, input().split()[:2])
    myGraph[x] = myGraph.setdefault(x, set()) | {y}
    myGraph[y] = myGraph.setdefault(y, set()) | {x}


def dfs(v, num):
    num += 1
    visited.add(v)

    if v == b:
        result.add(num)

    nbr = myGraph[v] - visited
    for v in nbr:
        dfs(v, num)


dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(max(result)-1)
