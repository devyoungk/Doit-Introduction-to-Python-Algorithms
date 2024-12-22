#랜덤한 값 중 최대값 찾기

import random
from max import max_of


print('난수의 최댓값을 구합니다.')
n = int(input('난수의 갯수: '))
l = int(input('난수 중 최소 값: '))
h = int(input('난수 중 최대 값: '))

x = [None] * n

for i in range(n):
    x[i] = random.randint(l, h)

print(x)
print(f'이 중 최댓값은 {max_of(x)}입니다.')
