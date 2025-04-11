# 10431번. 줄세우기

import sys
input = sys.stdin.readline

p = int(input())

for _ in range(p):
    data = list(map(int, input().split()))
    test_num = data[0]
    cnt = 0     # 이동 횟수, insert 횟수
    
    line = []
    for h in data[1:]:
        # 적절한 위치 찾고 line에 삽입
        # 줄에서 삽입 위치 탐색
        for i in range(len(line)):
            if line[i] > h:
                line.insert(i, h)
                cnt += len(line) - i - 1
                break
        else:
            # break가 한 번도 발생하지 않았을 때 실행됨.
            line.append(h)

    print(test_num, cnt)
    