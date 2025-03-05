# 회사에 있는 사람

n = int(input())

dic = {}
for i in range(n):
    name, status = map(str, input().split())
    if status == "enter":
        dic[name] = 1
    else:
        dic[name] = 0

sdic = sorted(dic.items(), reverse=True)

for i in sdic:
    if dic[i[0]] == 1:
        print(i[0])

