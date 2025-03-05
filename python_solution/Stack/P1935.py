# 1935번. 후위 표기식2
from collections import deque

n = int(input())  # 피연산자의 개수
s = input().strip()  # 후위 표기식

operand = [int(input()) for _ in range(n)]
stack = deque()

for i in s:
    if 'A' <= i <= 'Z':
        stack.append(operand[ord(i) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            a += b
        elif i == '-':
            a -= b
        elif i == '*':
            a *= b
        elif i == '/':
            a /= b
        stack.append(a)

print('%.2f' % stack[0])

