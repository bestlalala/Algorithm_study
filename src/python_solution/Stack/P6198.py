# 6198번 옥상 공원 꾸미기

n = int(input())
buildings = [int(input()) for i in range(n)]

stack = []
result = 0

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    result += len(stack)-1

print(result)



