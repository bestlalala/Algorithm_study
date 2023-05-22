# 정수 삼각형

n = int(input())

s = []
for i in range(1, n+1):
    s.append([int(m) for m in input().split()[:i]])

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            s[i][j] += s[i-1][j]
        elif j == i:
            s[i][j] += s[i-1][j-1]
        else:
            s[i][j] += max(s[i-1][j-1], s[i-1][j])

print(max(s[n-1]))

