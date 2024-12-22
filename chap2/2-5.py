#튜플, 문자열, 문자열 리스트의 최댓값은?

from max import max_of

a = (1, 2, 3, 7.5, 6.3)
b = 'python'
c = 'PyThoN'
d = ['ABCD', 'XYZ', 'ZXCV']

print(f'{a}의 최댓값은 {max_of(a)}입니다.') #가장 큰 실수
print(f'{b}의 최댓값은 {max_of(b)}입니다.') #알파벳 순
print(f'{c}의 최댓값은 {max_of(c)}입니다.') #대소문자는 의미 없어
print(f'{d}의 최댓값은 {max_of(d)}입니다.') #사전 순
