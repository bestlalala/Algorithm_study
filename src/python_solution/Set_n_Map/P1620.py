# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dogam = dict()
for i in range(n):
    s = input().strip()
    dogam[s] = i+1
revers_dogam = dict(map(reversed, dogam.items()))

pocketmon = list()
for _ in range(m):
    pocketmon.append(input().strip())

for p in pocketmon:
    if p.isdigit():
        print(revers_dogam[int(p)])
    else:
        print(dogam[p])



