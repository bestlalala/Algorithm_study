# 8980번. 택배

n, c = map(int, input().split())
m = int(input())
posts = [[int(p) for p in input().split()] for _ in range(m)]
posts.sort(key=lambda x: x[1])

truck = [c]*n
cnt = 0


for fr, to, box in posts:
    _min = c
    for i in range(fr, to):
        if _min > min(truck[i], box):
            _min = min(truck[i], box)
    for i in range(fr, to):
        truck[i] -= _min
    cnt += _min
print(cnt)
