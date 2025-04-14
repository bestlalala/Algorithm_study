# 1244번. 스위치 켜고 끄기

import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

m = int(input())
student = [list(map(int, input().split())) for _ in range(m)]

# 스위치 상태 바꾸기
def turn(num):
    # print("turn num", num)
    if switch[num]:
        switch[num] = 0
    else:
        switch[num] = 1
    # print(switch)

for s, num in student:
    if s == 1:
        # s의 배수 번호 스위치 상태 바꾸기
        for i in range(num, n+1, num):
            turn(i-1)
        # print(switch)
    elif s == 2:
        # 대칭 확인 -> 스위치 상태 바꾸기
        turn(num-1)
        for i in range(1, n):
            if 0 <= num - i - 1 and num + i - 1 < n:
                if switch[num-i-1] == switch[num+i-1]:
                    turn(num-i-1)
                    turn(num+i-1)
                else:
                    break
            else:
                break
        # print(switch)

for i in range(n):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:     # i+1로 하지 않으면 i=0 일 때 줄바꿈 발생
        print()