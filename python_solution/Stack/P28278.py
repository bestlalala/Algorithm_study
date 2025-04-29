# 28278번. 스택 2

import sys
input = sys.stdin.readline

stack = []

n = int(input())
for _ in range(n):
    tokens = input().split()
    
    if tokens[0] == '1':
        stack.append(int(tokens[1]))
    elif tokens[0] == '2':
        print(stack.pop() if stack else -1)
    elif tokens[0] == '3':
        print(len(stack))
    elif tokens[0] == '4':
        print(0 if stack else 1)
    elif tokens[0] == '5':
        print(stack[-1] if stack else -1)
