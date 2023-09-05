# 1931번. 회의실 배정

n = int(input())
times = [[int(m) for m in input().split()] for _ in range(n)]

times.sort(key=lambda x: x[0])  # 시작시간 기준 오름차순 정렬
times.sort(key=lambda x: x[1])  # 종료시간 기준 오름차순 정렬

last = 0    # 회의의 마지막 시간을 저장할 변수
count = 0   # 회의 개수를 저장할 변수

for s, e in times:
    # 시작 시간이 이전 회의의 마지막 시간보다 크거나 같을 경우
    if s >= last:
        count += 1
        last = e

print(count)

