# 1700번. 멀티탭 스케줄링

n, k = map(int, input().split())
elecs = [int(e) for e in input().split()]

cnt = 0
multitab = []

while elecs:

    now = elecs.pop(0)

    # 이미 꽂혀 있는 경우
    if now in multitab:
        continue

    # 빈 플러그가 있으면 거기에 꽂는다.
    if len(multitab) < n:
        multitab.append(now)

    else:
        change = 0
        max_idx = -1
        # 빈 플러그가 없는 경우
        for m in multitab:
            # 다시 쓸 일이 없으면 뽑는다.
            if m not in elecs:
                change = m
                break
            elif elecs.index(m) > max_idx:
                max_idx = elecs.index(m)
                change = m
        multitab[multitab.index(change)] = now
        cnt += 1

print(cnt)
