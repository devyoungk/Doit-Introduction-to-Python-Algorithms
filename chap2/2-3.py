#모듈 테스트

from max import max_of #모듈명은 숫자로 시작할 수 없다?? 소문자로 구성

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                  

while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
   # if not int(s):
   #     s = input(f'x[{number}]를 다시 입력하세요.: ') #정수가 아닌 것을 입력시 오류가 나지 않게 하는 법 찾아보기
    x.append(int(s))    
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')
