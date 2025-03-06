# 1789번. 수들의 합
import sys
input = sys.stdin.readline

s = int(input().rstrip())

result = 0
n = 0

# 1부터 차례대로 더하다가 s보다 커지는 순간 stop
while result <= s:
    n += 1
    result += n
    
print(n-1)