# 1439번. 뒤집기

S = input()
len_S = len(S)
one_list = [v for v in S.split("0") if v]
zero_list = [v for v in S.split("1") if v]

# print(zero_list)
# print(one_list)

print(min(len(zero_list), len(one_list)))
