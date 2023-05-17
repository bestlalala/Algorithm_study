# 듣보잡
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
neverHeard = set()
neverSeen = set()

for _ in range(n):
    neverHeard.add(input().strip())

for _ in range(m):
    neverSeen.add(input().strip())

neverHeardSeen = neverHeard & neverSeen

print(len(neverHeardSeen))
for i in sorted(neverHeardSeen):
    print(i)
