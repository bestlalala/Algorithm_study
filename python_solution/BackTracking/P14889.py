# 14889번. 스타트와 링크

import sys
input = sys.stdin.readline

# 팀의 능력치 = 팀에 속한 모든 쌍의 능력치 Sij의 합
# i, j가 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij + Sji
# 두 팀의 능력치 차이의 최솟값

n = int(input().rstrip())
s = [list(map(int, input().rstrip().split())) for _ in range(n)]

min_diff = float('inf')
team_size = n//2
visited = [False] * n   # 방문 체크 배열

def teamPower(team):
    power = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            power += s[team[i]][team[j]] + s[team[j]][team[i]]
    return power

def backtrack(idx, cnt):
    global min_diff
    
    # 팀원 수가 채워진 경우
    if cnt == team_size:
        team1, team2 = [], []
        
        for i in range(n):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        
        # 능력치 계산
        power1 = teamPower(team1)
        power2 = teamPower(team2)
        
        min_diff = min(min_diff, abs(power1-power2))
        return
    
    # 가능한 모든 경우 탐색
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtrack(i + 1, cnt + 1)
            visited[i] = False

backtrack(0, 0)
print(min_diff)