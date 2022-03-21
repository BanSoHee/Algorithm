## 기본 수학2 - 베르트랑 공준

isprime_list = []

## 지정 범위의 수를 소수인지 아닌지 미리 판별.
def isprime(num):
    if num == 1: return False
    if num == 2: return True

    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            #print(i, num%i)
            return False
    else:
        return True

for i in range(1, 2*123456+1):
    if isprime(i):
        isprime_list.append(True)
    else:
        isprime_list.append(False)

## main code.   
while True:
    n = int(input())
    if n == 0:
        break
    print(isprime_list[n:2*n].count(True))