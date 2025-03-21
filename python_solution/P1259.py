# 1259번. 팰린드롬수

import sys
from collections import deque
input = sys.stdin.readline

while True:
    num = input().rstrip()
    
    if num == '0':
        break
    
    half = len(num)//2
    
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
    
    # if len(num) == 1:
    #     print('yes')
    #     continue
    # elif len(num) == 2:
    #     if num[0] == num[1]:
    #         print('yes')
    #     else:
    #         print('no')
    #     continue
    # elif len(num) == 3:
    #     if num[0] == num[2]:
    #         print('yes')
    #     else:
    #         print('no')
    #     continue
        
    # # 인덱스: [길이//2] 까지 스택에 넣기
    # # 하나씩 꺼내서 비교
    
    # stack = deque()

    # if len(num) % 2 == 0:
    #     for i in range(half):
    #         stack.append(num[i])
    # else:
    #     for i in range(half + 1):
    #         stack.append(num[i])
    
    # result = "yes"
    # for i in range(half, len(num)):
    #     if num[i] != stack.pop():
    #         result = "no"
            
    # print(result)