# 15650번 N과 M(2)

n, m = map(int, input().split())
cnt = 0
s = []


def solve(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            solve(i + 1)
            s.pop()


solve(1)
