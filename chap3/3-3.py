#선형 검색 알고리즘(보초법)
from typing import Sequence, Any
import copy

def search(a: Sequence, key: Any) -> int:

    b = copy.deepcopy(a)
    b.append(key)

    i = 0
    while True:
        if b[i] == key:
            break
        i += 1

    if i == len(a):
        return 0
    else : return i


if __name__ == '__main__':
    n = int(input('원소의 수를 입력하세요.: '))

    x = [None] * n

    for i in range(n):
            x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    k = int(input('검색할 값을 입력하세요.: '))

    idx = search(x, k)
    if idx == 0:
            print(f'{k}은(는) 존재하지 않습니다.')

    else :
        print(f'검색 결과 {k}는 x[{idx}]에 있습니다.')


