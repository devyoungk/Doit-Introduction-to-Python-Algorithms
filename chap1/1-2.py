#세 정수의 최댓값 함수 정의

def max(a, b, c):
    max = a
    if b > max : max = b
    if c > max : max = c
    return max

# print(f'max(1,2,3) = {max(1,2,3)}')

print('세 정수를 입력하세요: ')
a = int(input())
b = int(input())
c = int(input())

print(f'max(a,b,c) = {max(a,b,c)}')
