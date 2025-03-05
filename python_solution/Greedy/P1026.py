# 1026번. 보물

n = int(input())
A = [int(m) for m in input().split()]
B = [int(m) for m in input().split()]

result = 0
for i in range(n):
    result += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(result)


