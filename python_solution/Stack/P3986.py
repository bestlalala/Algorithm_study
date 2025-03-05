# 3986번 좋은 단어
from collections import deque

n = int(input())    # 단어의 수
word_list = [input() for _ in range(n)]     # 단어 리스트

result = 0

for word in word_list:
    stack = deque()
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        result += 1

print(result)

