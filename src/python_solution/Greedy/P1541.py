# 1541번. 잃어버린 괄호

sik = input().split('-')
result = 0

for i in sik[0].split('+'):
    result += int(i)
for i in sik[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
