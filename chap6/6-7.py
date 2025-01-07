from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    for i in range (1,n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬 프로그램')
    n = int(input('원소 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]을 입력하세요.: '))

    insertion_sort(x)

    print('정렬 결과입니다.')

    print(x)
