#선형 검색 알고리즘
from typing import Sequence, Any

def search(a: Sequence, key: Any) -> int:

    i = 0

    while True:
        if i==len(a):
            return -1
        if a[i] == key:
            return i
        i += 1



if __name__ == '__main__':
    n = int(input('원소의 수를 입력하세요.: '))

    x = [None] * n

    for i in range(n):
            x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    k = int(input('검색할 값을 입력하세요.: '))

    if search(x, k) == -1:
            print(f'{k}은(는) 존재하지 않습니다.')

    else :
        print(f'검색 결과 {k}는 x[{search(x, k)}]에 있습니다.')
