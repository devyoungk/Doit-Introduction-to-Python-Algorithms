#선형 검색 알고리즘(for문)

from typing import Sequence, Any

def search(a: Sequence, key: Any) -> int:

    for i in range (len(a)):
        if a[i] == key:
            return i

    return 0



if __name__ == '__main__':
    n = int(input('원소의 수를 입력하세요.: '))

    x = [None] * n

    for i in range(n):
            x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    k = int(input('검색할 값을 입력하세요.: '))

    if search(x, k) == 0:
            print(f'{k}은(는) 존재하지 않습니다.')

    else :
        print(f'검색 결과 {k}는 x[{search(x, k)}]에 있습니다.')
