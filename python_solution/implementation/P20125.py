# 10125번. 쿠키의 신체 측정

import sys
input = sys.stdin.readline

n = int(input())
cookie = [input() for _ in range(n)]

center = tuple()
left_arm, right_arm, left_leg, right_leg, waist = 0, 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            if not center:
                center = (i, j)
            elif center:
                if i == center[0]+1: 
                    if j < center[1]:
                        left_arm += 1
                    elif j > center[1]:
                        right_arm += 1
                else:
                    if j == center[1]:
                        waist += 1
                    elif j == center[1] - 1:
                        left_leg += 1
                    elif j == center[1] + 1:
                        right_leg += 1

print(center[0]+2, center[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)