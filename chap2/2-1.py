#5명의 시험점수 합계와 평균 구하기

print('시험 점수의 합계와 평균을 구합니다.')

score1 = int(input('첫 번째 학생의 점수를 입력하세요. : '))
score2 = int(input('두 번째 학생의 점수를 입력하세요. : '))
score3 = int(input('세 번째 학생의 점수를 입력하세요. : '))
score4 = int(input('네 번째 학생의 점수를 입력하세요. : '))
score5 = int(input('다섯 번째 학생의 점수를 입력하세요. : '))

sum = score1 + score2 + score3 + score4 + score5
avg = sum/5

print(f'시험 점수의 합계는 {sum}입니다.')
print(f'시험 점수의 평균은 {avg}입니다.')
