# 2457번. 공주님의 정원
import sys
input = sys.stdin.readline

n = int(input())
dates = []
for _ in range(n):
    temp = [int(m) for m in input().split()]
    dates.append([temp[0]*100 + temp[1], temp[2]*100 + temp[3]])

dates.sort(key=lambda x: (x[0], x[1]))


end = 0    # 제일 늦게 지는 꽃 비교
target = 301    # 마지막 꽃의 지는 날
cnt = 0

while dates:
    # 마지막 꽃의 지는 날이 12월 1일보다 크거나 같을 때와
    # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
    if target >= 1201 or target < dates[0][0]:
        break

    # 꽃 개수의 길이만큼 반복하여 구간별로 꽃을 비교한다.
    for _ in range(len(dates)):
        # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 크거나 같으면 그 꽃의 지는 날을 확인한다.
        if target >= dates[0][0]:
            if end <= dates[0][1]:
                end = dates[0][1]

            # 꽃을 확인하면 제거한다.
            dates.pop(0)
        else:   # 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
            break

    # 최종적으로 선택한 꽃의 지는 날을 바꾼다.
    target = end
    cnt += 1

# 마지막 꽃의 지는 날이 12월 1일보다 작으면 11월 30일에는 피어있는 꽃이 없기 때문에 0 출력
if target < 1201:
    print(0)
else:
    print(cnt)
