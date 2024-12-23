#10진수 정수를 다른 진수로 변환

def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #36진수까지 가능

    while x > 0:
        d += dchar[x % r] # r로 나눈 나머지 값 d에 추가
        x = x//r #몫을 x로 변환 후 반복

    return d[::-1] #진수 변환 시 역순으로 출력해야 

#test
print(card_conv(7, 2))
print(card_conv(10, 2))
print(card_conv(11, 2))
print(card_conv(15, 2))
