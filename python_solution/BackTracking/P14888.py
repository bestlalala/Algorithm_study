# 14888번. 연산자 끼워넣기

import sys
input = sys.stdin.readline

# 수와 수 사이에 연산자를 하나씩 넣어서, 수식 만들기
# 주어진 수의 순서는 바꾸면 안 됨
# 연산자 우선순위 무시하고 앞에서부터 진행
# N개의 수와 N-1개의 연산자 주어짐
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것 구하기

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
# +, -, x, /
counts = list(map(int, input().rstrip().split()))

max_value, min_value = -float('inf'), float('inf')

# 연산
def backtrack(cur_value, idx, ops): # 지금까지 계산한 값, 현재 사용할 숫자의 인덱스, 연산자 개수 배열
    global max_value, min_value
    
    # 종료 조건: 숫자 연산 다 했을 때
    if idx == n:
        max_value = max(max_value, cur_value)
        min_value = min(min_value, cur_value)
        return
    
    # 현재 숫자
    num = nums[idx]

    # 가능한 모든 선택지들 탐색: 연산자 하나씩 넣어보기
    if ops[0] > 0:
        ops[0] -= 1
        backtrack(cur_value + num, idx + 1, ops)
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        backtrack(cur_value - num, idx + 1, ops)
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        backtrack(cur_value * num, idx + 1, ops)
        ops[2] += 1
    # 나눗셈: 정수 나눗셈으로 몫만 취하기 (//)
    if ops[3] > 0:
        ops[3] -= 1
        if cur_value > 0:
            backtrack(cur_value // num, idx + 1, ops)
        else:    # 음수 // 양수 -> - (양수 // 양수)
            backtrack(-(-cur_value // num), idx + 1, ops)
        ops[3] += 1

backtrack(nums[0], 1, counts)
print(max_value)
print(min_value)