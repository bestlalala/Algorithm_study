# 7570번. 줄 세우기

n = int(input())
children = [int(c) for c in input().split()]

idx = [-1] * (n+1)

for i, v in enumerate(children):
    idx[v] = i  # 각 번호가 현재 children 배열에서 어떤 위치에 있는지 기록

longest = 0
cnt = 1

for c in range(1, n):
    # 번호 i
    if idx[c] < idx[c+1]:
        cnt += 1
    else:
        longest = max(longest, cnt)
        cnt = 1

print(n-longest if n != 1 else 0)
