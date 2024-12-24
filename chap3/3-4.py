#이진 검색 알고리즘
from typing import Sequence, Any

def bin_search(a: Sequence, key: Any) -> int:

    pl = 0
    pr = len(a)-1

    while True:
        pc = (pl + pr)//2
        if a[pc] == key :
            return pc
        elif a[pc] < key :
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr :
            break
    return -1



if __name__ == '__main__':
    n = int(input('원소의 수를 입력하세요.: '))

    x = [None] * n

    print('데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]를 입력하세요.: '))

    for i in range(1, n):
        while True:
            x[i] = int(input(f'x[{i}]를 입력하세요.: '))
            if x[i] < x[i-1]:
                print('오름차순이 아닙니다. 다시 입력하세요.')
            else:
                break

    k = int(input('검색할 값을 입력하세요.: '))

    idx = bin_search(x, k)
    if idx == -1 :
            print(f'{k}은(는) 존재하지 않습니다.')

    else :
        print(f'검색 결과 {k}는 x[{idx}]에 있습니다.')
