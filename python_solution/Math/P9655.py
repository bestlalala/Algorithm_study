# 9655번. 돌 게임

import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n % 2 == 0:
    print("CY")
else:
    print("SK")