# 21735번. 눈덩이 굴리기

n, m = map(int, input().split())
a = [0] + [int(n) for n in input().split()]

snowball = 1
loc = 0


def dfs(index, size, time):
    global ans  # 답

    if time > m:
        return

    if time <= m:
        ans = max(ans, size)

    # 눈덩이 굴리기
    if index <= n-1:
        dfs(index+1, size+a[index+1], time+1)

    # 눈덩이 던지기
    if index <= n-2:
        dfs(index+2, size//2 + a[index+2], time+1)

ans = -1

dfs(0, 1, 0)
print(ans)
