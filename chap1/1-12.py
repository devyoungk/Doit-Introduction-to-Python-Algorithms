# + - 번갈아 출력하기

#홀짝

print('+와 -를 반복 출력하는 프로그램입니다.')
n=int(input('몇 개까지 출력할까요? : '))

str=''
for i in range (n//2):
    str += '+-'
if n%2 == 1:
    str += '+'

print(str)
