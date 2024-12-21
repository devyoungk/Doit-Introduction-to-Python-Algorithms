#가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('area를 입력하세요(자연수) : '))

i=1
while (i*i <= area):
    if area%i == 0:
        print(f'{i} x {area//i} = {area}')
    i += 1
