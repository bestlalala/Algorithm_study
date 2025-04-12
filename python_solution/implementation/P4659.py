# 4659번. 비밀번호 발음하기

import sys
input = sys.stdin.readline

vowel = set('aeiou')

while True:
    pw = input().rstrip()
    if pw == 'end':
        break
    else:
        has_vowel = False
        is_valid = True
        
        vowel_cnt = 0   # 연속된 모음 개수
        consonant_cnt = 0   # 연속된 자음 개수
        
        prev = ''   # 이전 값
        
        for c in pw:
            # 모음 체크
            if c in vowel:
                has_vowel = True
                vowel_cnt += 1
                consonant_cnt = 0
            else:
                vowel_cnt = 0
                consonant_cnt += 1
            
            # 모음 연속 3개 or 자음 연속 3개
            if vowel_cnt == 3 or consonant_cnt == 3:
                is_valid = False
                break
            
            
            # 같은 글자 연속 2번 X (ee, oo 는 허용)
            if c == prev and c not in ('e', 'o'):
                is_valid = False
                break
                
            prev = c
                

        if has_vowel and is_valid:
            print(f'<{pw}> is acceptable.')
        else:
            print(f'<{pw}> is not acceptable.')
            
        