# 서로 다른 부분 문자열의 개수

s = input()
str = set()
l = len(s)

for i in range(l):
    for j in range(i, l):
        str.add(s[i:j+1])

print(len(str))
