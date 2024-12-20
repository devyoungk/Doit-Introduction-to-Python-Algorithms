#*을 n개 출력하되 w개마다 줄바꿈하기

n = int(input('*을 n개 출력하는 프로그램입니다. n값을 입력하세요. : '))
w = int(input('몇 개마다 줄바꿈할까요? :'))

for _ in range (n//w):
    print('*'*w)
x = n%w
if x : print ('*'*x)

    
            
