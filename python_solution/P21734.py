# SMUPC 대회 문제 - SMUPC의 등장

def print_n(s):
    for i in range(a):
        print(s, end="")
    print("")

input_S = input()
list = list(input_S)

for s in input_S:
    n = ord(s)
    a = 0
    while n > 0:
        a += n % 10
        n //= 10
    print_n(s)
