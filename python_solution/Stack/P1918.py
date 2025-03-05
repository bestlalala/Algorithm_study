# 1918번. 후위 표기식
from collections import deque
s = input()

stack = deque()
ans = ''
for i in s:
    if i.isalpha():
        ans += i
    else:
        if i == '(':    # 괄호 먼저 확인
            stack.append(i)
        elif i == '*' or i == '/':
            # stack 이 비어 있지 않고, top 이 '*' 또는 '/' 때까지 pop
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':  # 가장 낮은 우선 순위의 연산자
            # stack 이 비어 있지 않고, top 이 '(' 일 때까지 pop
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()

print(ans)

