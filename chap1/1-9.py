#a부터 b까지 합

print('a부터 b까지의 합을 구하는 프로그램입니다.')
a = int(input('a값을 입력해주세요: '))
b = int(input('b값을 입력해주세요: '))

if a > b :
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}부터 {b}까지의 합은 {sum}입니다.')
