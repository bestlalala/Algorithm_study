# 2493번. 탑

n = int(input())
tops = [int(i) for i in input().split()]

stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tops[i]])

print(*answer)
