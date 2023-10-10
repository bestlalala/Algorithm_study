# 9205번. 맥주 마시면서 걸어가기
from collections import deque


def bfs():
    que = deque()
    que.append(home)
    visited = set()

    while que:
        x, y = que.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if shop[i] not in visited:
                nx, ny = shop[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited.add((nx, ny))
                    que.append((nx, ny))
    print('sad')
    return


t = int(input())    # 테스트 케이스 개수

for _ in range(t):
    n = int(input())  # 편의점의 수
    home = tuple(int(m) for m in input().split())  # 상근이네 집
    shop = []
    for _ in range(n):
        shop.append(tuple(int(m) for m in input().split()))
    festival = tuple(int(m) for m in input().split())
    bfs()
