# 9663번. N-Queen

import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 열 체크 (퀸이 놓인 열 표시)
check_column = [0] * n
# y = -x 방향의 대각선을 체크하는 배열 (오른쪽 위 → 왼쪽 아래)
# 대각선의 값은 (row - col)으로 계산됨
# 예를 들어, (0, 0), (1, 1), (2, 2) 같은 위치들이 같은 대각선에 있음
# 이 값은 음수가 될 수 있으므로, 인덱스를 양수로 만들기 위해 (n - 1)을 더해줌
# 최소값: -(n-1), 최대값: n-1 => 총 크기: 2n - 1
check_leftcross = [0] * (2 * n - 1)

# y = x 방향의 대각선을 체크하는 배열 (왼쪽 위 → 오른쪽 아래)
# 대각선의 값은 (row + col)으로 계산됨
# 예를 들어, (0, 0), (1, 1), (2, 2) 같은 위치들이 같은 대각선에 있음
# 이 값은 항상 0 이상이므로 추가 조정 없이 사용 가능
# 최소값: 0, 최대값: 2(n-1) => 총 크기: 2n - 1
check_rightcross = [0] * (2 * n - 1)

def backtrack(cur, res):
    # 모든 행에 퀸을 배치한 경우 (성공적으로 퀸을 배치했을 때)
    if cur == n:
        return res + 1  # 경우의 수를 1 증가시킴
    
    for i in range(n):  # 각 행에서 모든 열을 확인
        # 만약 현재 위치에 퀸을 놓으면, 두 대각선 중 하나에 겹치는 경우라면 건너뜀
        if check_column[i] or check_leftcross[cur - i + (n - 1)] or check_rightcross[cur + i]:
            continue  # 퀸을 놓을 수 없는 위치이므로 다음 열로 넘어감
        
        # 현재 위치에 퀸을 배치한다고 표시
        check_column[i] = 1
        check_leftcross[cur - i + (n - 1)] = 1  # 왼쪽 대각선 체크
        check_rightcross[cur + i] = 1  # 오른쪽 대각선 체크
        
        # 다음 행으로 이동하여 퀸을 배치하기 (재귀 호출)
        res = backtrack(cur + 1, res)
        
        # 퀸을 배치하고 되돌아왔으니, 현재 위치 표시 제거 (백트래킹)
        check_column[i] = 0
        check_leftcross[cur - i + (n - 1)] = 0
        check_rightcross[cur + i] = 0
    
    # 현재 경로로 찾은 경우의 수 반환
    return res

# 대칭성을 활용한 경우의 수 계산
result = 0

# 좌측 절반의 열만 탐색하고 결과를 두 배로 함
for i in range(n // 2):
    check_column[i] = 1
    check_leftcross[0 - i + (n - 1)] = 1
    check_rightcross[0 + i] = 1
    result += backtrack(1, 0)
    
    # 백트래킹으로 원상복구
    check_column[i] = 0
    check_leftcross[0 - i + (n - 1)] = 0
    check_rightcross[0 + i] = 0

result *= 2  # 대칭성을 활용해 얻은 결과를 두 배로 늘림

# n이 홀수일 때, 가운데 열은 대칭성이 없으므로 따로 계산
if n % 2 == 1:
    mid = n // 2
    check_column[mid] = 1
    check_leftcross[0 - mid + (n - 1)] = 1
    check_rightcross[0 + mid] = 1
    result += backtrack(1, 0)
    
    # 백트래킹으로 원상복구
    check_column[mid] = 0
    check_leftcross[0 - mid + (n - 1)] = 0
    check_rightcross[0 + mid] = 0

print(result)