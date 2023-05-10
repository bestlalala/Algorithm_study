# 소트인사이드

n = input()


num = []
for i in n:
    num.append(int(i))

num.sort(reverse=True)

for i in num:
    print(i, end='')
