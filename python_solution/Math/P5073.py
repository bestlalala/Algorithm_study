# 5073번. 삼각형과 세 변

import sys
input = sys.stdin.readline

def check(line_list):
    line_list.sort()
    a, b, c = line_list[0], line_list[1], line_list[2]
    
    if a == b == c:
        print("Equilateral")
    elif c < a + b:
        if a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")

    
while True:
    lines = list(int(i) for i in input().rstrip().split())
    if sum(lines) == 0:
        break
    else:
        check(lines)