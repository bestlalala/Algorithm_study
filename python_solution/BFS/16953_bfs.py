# 16953번. A->B

import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

def bfs(a, b):
    que = deque([(a, 1)])   # (현재 값, 연산 횟수)
    
    while que:
        n, cnt = que.popleft()
        
        if n == b:
            return cnt
        
        # 2를 곱하기
        if n * 2 <= b:
            que.append((n*2, cnt + 1))
        
        # 1을 수의 가장 오른쪽에 추가하기
        if n * 10 + 1 <= b:
            que.append((n * 10 + 1, cnt + 1))
        
    return -1

print(bfs(a, b))    
