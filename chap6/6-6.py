from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    for i in range (n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

if __name__ == '__main__':
    print('단순 선택 정렬 프로그램')
    n = int(input('원소 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]을 입력하세요.: '))

    selection_sort(x)

    print('정렬 결과입니다.')

    print(x)
