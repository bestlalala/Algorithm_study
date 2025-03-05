# 3015번. 오아시스 재결합
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())    # 기다리고 있는 사람의 수
people = [int(input()) for _ in range(n)]   # 각 사람의 키

stack = deque()  # (키, cnt)로 append
ans = 0

for p in people:
    # 스택의 끝 값이 더 클 때까지 pop
    while stack and stack[-1][0] < p:
        ans += stack.pop()[1]   # pop된 요소의 cnt

    # 스택이 비어있으면 해당 키 append하고 continue
    if not stack:
        stack.append((p, 1))
        continue

    # 스택 끝 값의 키와 같을 때
    if stack[-1][0] == p:
        cnt = stack.pop()[1]
        ans += cnt

        if stack:
            ans += 1
        stack.append((p, cnt + 1))

    # 스택 끝 값의 키보다 작을 때
    else:
        stack.append((p, 1))
        ans += 1

print(ans)


