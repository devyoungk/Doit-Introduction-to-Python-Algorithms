def mov(no: int, x: int, y: int) -> None: #원반 no개를 x에서 y로 이동
    if no > 1:
        mov(no-1, x, 6-x-y) #(no-1)개를 x,y를 제외한 곳으로 이동
    print(f'{no}을(를) {x}에서 {y}로 이동')
    if no > 1:
        mov(no-1, 6-x-y, y) #옮겨둔 (no-1)개를 y위로 이동

print('하노이의 탑')
n = int(input('원반의 개수를 입력하세요. : '))

mov(n, 1, 3)

    
