#1000이하의 소수 나열

for n in range(2, 1001):
    for i in range(2, n):
        if n % i == 0:
            break
    else :
        print(n)


#소수인지 확인하려면 다른 소수의 배수가 아닌것을 확인하면 된다.

