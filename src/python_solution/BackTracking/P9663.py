# 9663번. N-Queen
import sys
input = sys.stdin.readline

"""
퀸이 서로 공격할 수 없도록 하는 방법
1. 같은 행에 위치X
2. 같은 열에 위치X
3. 대각선 상에 위치X
"""


n = int(input())
check_row = [0 for i in range(n)]
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]
ret = 0


def backtracking(cur):
    if cur == n:
        global ret
        ret += 1
        return 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0


for i in range(n//2):
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0
ret = ret*2

if n%2: #홀수일경우
    i = n // 2
    check_row[i] = 1
    check_leftcross[n - i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n - i] = 0
    check_rightcross[i] = 0

print(ret)
