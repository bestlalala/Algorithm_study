# 4779번. 칸토어 집합

import sys
input = sys.stdin.readline

def initialize(n):
    return '-' * pow(3, n)

def operation(res):
    if len(res) == 1:
        return res
    else:
        # 가운데 문자열을 공백으로 바꾸기
        pnt1 = len(res)//3
        pnt2 = pnt1 * 2
        return operation(res[:pnt1]) + ' ' * pnt1 + operation(res[pnt2:])

while True:
    n = input().rstrip()
    if n == '':
        break
    n = int(n)
    print(operation(initialize(n)))
    