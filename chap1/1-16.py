#1부터 n까지의 합(n은 양수)

print('1부터 n까지의 합을 구하는 프로그램입니다. n값을 입력해주세요. : ')
n=int(input())

while n<=0:
    print('다시 입력해주세요. : ')
    n=int(input())

sum = 0

for i in range(1,n+1):
    sum += i

print(f'1부터 {n}까지의 합은 {sum}입니다.')    
