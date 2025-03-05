# 숫자 카드 2

n = int(input())
card = [int(c) for c in input().split()]
card_dic = dict()
for c in card:
    if card_dic.get(c):
        card_dic[c] += 1
    else:
        card_dic[c] = 1

m = int(input())
todo = [int(t) for t in input().split()]


for i in todo:
    if card_dic.get(i):
        print(card_dic[i], end=' ')
    else:
        print(0, end=' ')

