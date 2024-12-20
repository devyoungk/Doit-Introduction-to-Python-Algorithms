#중앙 값 구하기

def median(a, b, c):
    if a >= b :
        if b >= c:
            return b
        elif a >= c:
            return c
        else : return a
    elif a >= c :
        return a
    elif  b >= c :
        return c
    else : return b



print('세 정수를 입력하세요')
a = int(input())
b = int(input())
c = int(input())

print(f'중앙 값은 {median(a,b,c)}입니다.')
