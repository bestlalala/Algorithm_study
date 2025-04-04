# 16139번. 인간-컴퓨터 상호작용

import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

# 알파벳의 개수 누적합
ps = [[0] * 26 for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    # print(s[i-1], ord(s[i-1]) - 97)
    
    for j in range(26):
        ps[i][j] = ps[i-1][j]
        if j == ord(s[i-1])-97:
            ps[i][j] += 1


for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    
    asc = ord(a) - 97
    print(ps[r+1][asc] - ps[l][asc])
