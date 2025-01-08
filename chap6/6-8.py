from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2

if __name__ == '__main__':
    print('셸 정렬 프로그램')
    n = int(input('원소 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]을 입력하세요.: '))

    shell_sort(x)

    print('정렬 결과입니다.')

    print(x)
