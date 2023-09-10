# 2847번. 게임을 만든 동준이

N = int(input())
score = [int(input()) for _ in range(N)]

cnt = 0
for i in reversed(range(N-1)):
    while score[i] >= score[i+1]:
        score[i] -= 1
        cnt += 1

print(cnt)
