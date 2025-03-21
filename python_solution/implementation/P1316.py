# 1316번. 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input().rstrip())
word = [input().rstrip() for _ in range(n)]

cnt = 0
for w in word:
    visited = []
    flag = True
    for i in range(len(w)):
        # 등장하지 않았던 문자
        if w[i] not in visited:
            visited.append(w[i])
        else:   # 등장했던 문자라면 이전 문자와 같은지 확인
            if w[i] != w[i-1]:
                flag = False
                break
    
    if flag:
        cnt += 1

print(cnt)