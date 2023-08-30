# 2217번. 로프

n = int(input())
weight = [int(input()) for _ in range(n)]

weight.sort()

max = 0
for i in range(n):
    w = weight[i] * (n-i)
    if w > max:
        max = w

print(max)

