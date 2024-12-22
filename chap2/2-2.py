#시퀀스에서 최댓값 찾기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    max = a[0]
    for i in range(1, len(a)):
         if a[i] > max: 
            max = a[i]
    return max

if __name__ == '__main__': #프로그램이 직접 실행될 때만 실행
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))
    
    print(f'최댓값은 {max_of(x)}입니다.')
