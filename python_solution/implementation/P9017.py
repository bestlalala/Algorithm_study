# 9017번. 크로스 컨트리

import sys
import collections
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    teams = list(map(int, input().split()))
    
    team = collections.Counter(teams)
    candidate_team = set(k for k, v in team.items() if v == 6)
    
    score =[[] for _ in range(n+1)]
    cnt = 1
    
    for t in teams:
        if t in candidate_team:
            score[t].append(cnt)
            cnt += 1
    
    win = (0, float('inf'))
    for i, s in enumerate(score):
        if len(s) == 6:
            sum_score = sum(s[:4])
            if sum_score < win[1]:
                win = (i, sum_score)
            elif sum_score == win[1]:
                if s[4] < score[win[0]][4]:
                    win = (i, sum_score)
    print(win[0])