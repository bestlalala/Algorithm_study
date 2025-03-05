# 커트라인

n, k = map(int, input().split())
score = [int(n) for n in input().split()]

score.sort(reverse=True)
print(score[k-1])

