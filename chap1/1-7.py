#1부터 n까지 합

print('1부터 n까지의 합을 구하는 프로그램입니다.')
n = int(input('n값을 입력하세요: '))

sum = 0
i = 1
while i <= n :
    sum += i
    i += 1

print(f'1부터 {n}까지의 합은 {sum}입니다.')

    
