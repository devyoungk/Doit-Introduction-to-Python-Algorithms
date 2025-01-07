from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1] :
                a[j], a[j-1] = a[j-1], a[j]

if __name__ == '__main__':
    print('버블 정렬 프로그램')
    n = int(input('원소 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]을 입력하세요.: '))

    bubble_sort(x)

    print('버블 정렬 결과입니다.')

    print(x)
