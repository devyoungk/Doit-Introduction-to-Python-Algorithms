def kmp_match(txt : str, pat: str) -> int:
    pt = 0 #txt 커서
    pp = 0 #pat 커서

    skip = [0] * (len(pat) + 1)  #건너뛰기 표

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

            
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요. : ')
    s2 = input('패턴을 입력하세요. : ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('해당 패턴이 존재하지 않습니다.')
    else:
        print(f'{idx+1}번째 문자가 일치합니다.')
