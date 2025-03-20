# 15686번. 치킨 배달

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

city = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 M개 선택
# 치킨 거리 구하기
# 모든 집의 치킨 거리의 합 -> 최솟값 저장

min_result = float('inf')

def dist(house, chicken_idx):
    city_dist = 0
    for r1, c1 in house:
        chick_dist = 2*n
        for i in chicken_idx:
            r2, c2 = chicken[i]
            chick_dist = min(chick_dist, abs(r1-r2)+abs(c1-c2))
        city_dist += chick_dist
    return city_dist

def backtrack(selected, start): # selected: 선택된 치킨집 인덱스 배열 
    global min_result
    
    # 치킨집 M개 선택 시 도시의 치킨 거리 계산
    if len(selected) == m:
        # 치킨 거리 계산
        min_result = min(min_result, dist(house, selected))
        return
    
    for i in range(start, len(chicken)):
        if i not in selected:
            selected.append(i)
            backtrack(selected, i+1)
            selected.pop()

chicken = []    # 치킨집 저장할 배열: (r, c)
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

backtrack([], 0)
print(min_result)