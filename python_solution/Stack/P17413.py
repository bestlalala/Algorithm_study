# 17413번. 단어 뒤집기 2
from collections import deque
import sys
S = sys.stdin.readline().strip() + ' '

stack = deque()
ans = ''
flag = 0    # 괄호 안에 있는지 여부

for i in S:
    if i == '<':
        flag = 1
        while stack:
            ans += stack.pop()
    stack.append(i)

    if i == '>':
        flag = 0
        while stack:
            ans += stack.popleft()

    if i == ' ' and flag == 0:
        stack.pop()
        while stack:
            ans += stack.pop()
        ans += ' '
print(ans)
