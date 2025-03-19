# 2630번. 색종이 만들기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

def color(p, size):
    # 배열 원소의 합이 0이거나 n*n
    sum_color = 0

    for i in range(size):
        sum_color += sum(p[i])

    if sum_color == 0:
        return 'W'
    elif sum_color == size * size:
        return 'B'
    else:
        return ''

white, blue = 0, 0
def backtrack(cur_paper):   # cur_paper: 쪼갠 현재 색종이
    global white, blue
    
    size = len(cur_paper)
    
    # 모두 같은 색인 경우 or 하나의 정사각형 칸인 경우
    if size == 1:
        if cur_paper[0][0] == 0:
            white += 1
        else:
            blue += 1
        return
    elif color(cur_paper, size) == 'W':
        white += 1
        return
    elif color(cur_paper, size) == 'B':
        blue += 1
        return
    
    # 종이 나누기
    half = size // 2
    temp = cur_paper
    # 1
    cur_paper = cur_paper[:half]
    for i in range(half):
        cur_paper[i] = cur_paper[i][:half]
    backtrack(cur_paper)
    cur_paper = temp
    
    # 2
    cur_paper = cur_paper[:half]
    for i in range(half):
        cur_paper[i] = cur_paper[i][half:]
    backtrack(cur_paper)
    cur_paper = temp
    
    # 3
    cur_paper = cur_paper[half:]
    for i in range(half):
        cur_paper[i] = cur_paper[i][:half]
    backtrack(cur_paper)
    cur_paper = temp
    
    # 4
    cur_paper = cur_paper[half:]
    for i in range(half):
        cur_paper[i] = cur_paper[i][half:]
    backtrack(cur_paper)
    cur_paper = temp

backtrack(paper)
print(white)
print(blue)
    