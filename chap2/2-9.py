#소수 구하기 알고리즘 개선

z = 0 #소수 카운트
prime = [None] * 500 #소수 저장
prime[0] = 2 #2는 첫 소수

z += 1

for n in range(3, 1001, 2): #짝수 배제 
    for i in range(1, z):
        if n % prime[i] == 0:
            break
    else :
        prime[z] = n
        z += 1

for i in range(z):
    print(prime[i])
