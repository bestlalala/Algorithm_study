# 1018번 체스판 다시 칠하기

import sys
input = sys.stdin.readline

# n: 행의 개수 (세로 크기), m: 열의 개수 (가로 크기)
n, m = map(int, input().rstrip().split())

# 보드 입력 받기 (n개의 문자열로 이루어진 리스트)
board = [input().rstrip() for _ in range(n)]

# 최소 다시 칠해야 하는 칸 수를 큰 값으로 초기화
min_paint = n * m

# 8x8 크기의 체스판을 만들 수 있는 모든 시작 좌표를 탐색
# 시작 좌표 (i, j)를 기준으로 8x8 크기 체스판을 잘라서 검사
for i in range(n - 7):
    for j in range(m - 7):
        # 두 가지 체스판 색칠 방법에 대한 칠해야 하는 칸 수
        paintW = 0  # 맨 왼쪽 위가 'W'인 경우
        paintB = 0  # 맨 왼쪽 위가 'B'인 경우

        # (i, j)부터 8x8 크기의 체스판 검사
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # (a + b) % 2 == 0인 칸은 맨 위쪽 칸과 같은 색이어야 함
                if (a + b) % 2 == 0:
                    # 맨 왼쪽 위가 'W'인 경우, 현재 칸도 'W'여야 함
                    if board[a][b] != 'W':  # 흰색이 아니라면 칠해야 함
                        paintW += 1  # 흰색으로 칠하기
                    # 맨 왼쪽 위가 'B'인 경우, 현재 칸도 'B'여야 함
                    else:  # 흰색이라면 칠해야 함
                        paintB += 1  # 검은색으로 칠하기
                # (a + b) % 2 == 1인 칸은 맨 위쪽 칸과 반대 색이어야 함
                else:
                    # 여기서도 두 가지 경우로 나뉨
                    # 맨 왼쪽 위가 'W'인 경우, 현재 칸은 'B'여야 함
                    if board[a][b] != 'B':  # 검은색이 아니라면 칠해야 함
                        paintW += 1  # 검은색으로 칠하기
                    # 맨 왼쪽 위가 'B'인 경우, 현재 칸은 'W'여야 함
                    else:  # 흰색이라면 칠해야 함
                        paintB += 1  # 흰색으로 칠하기
        
        # 두 가지 경우 중 최소값을 저장
        min_paint = min(min_paint, paintW, paintB)

# 최소 칠해야 하는 칸 수 출력
print(min_paint)

