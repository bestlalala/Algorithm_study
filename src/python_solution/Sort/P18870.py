# 좌표 압축
import sys
input = sys.stdin.readline

n = int(input())
x_list = [int(x) for x in input().split()]

sorted_list = sorted(set(x_list))

dic = {sorted_list[i]: i for i in range(len(sorted_list))}

for x in x_list:
    print(dic[x], end=' ')

