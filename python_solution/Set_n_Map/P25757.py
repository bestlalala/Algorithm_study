# 25757번. 임스와 함께하는 미니게임

n, k = input().split()
n = int(n)

game = {'Y': 1, 'F': 2, 'O': 3}
mate = set()
for _ in range(n):
    p = input().rstrip()
    mate.add(p)

print(len(mate)//game[k])  