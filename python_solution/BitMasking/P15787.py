# 15787번. 기차가 어둠을 헤치고 은하수를

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
command = [list(map(int, input().split())) for _ in range(m)]

# print(command)
train = [0] * n

# 기차가 지나갈 때 승객이 앉은 상태를 목록에 기록
for c in command:
    if c[0] == 1:
        if not (train[c[1]-1] & (1 << (c[2] - 1))):
            train[c[1]-1] += 1 << (c[2] - 1)
    elif c[0] == 2:
        if train[c[1]-1] & (1 << c[2] - 1):
            train[c[1]-1] -= 1 << (c[2] - 1)
    elif c[0] == 3:
        # i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로 이동 (k -> k+1)
        train[c[1]-1] <<= 1
        train[c[1]-1] &= 0xfffff
    elif c[0] == 4:
        train[c[1]-1] >>= 1
    # print(train)

result = set(train)
print(len(result))