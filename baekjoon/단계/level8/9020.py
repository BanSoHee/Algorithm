## 기본 수학2 - 골드바흐의 추측

isprime_list = [2] # 0은 소수가 아님.

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

for i in range(3, 10000, 2): # 1 ~ 10000 중 소수를 담은 리스트 생성.
    if isprime(i):
        isprime_list.append(i)

T = int(input())
for i in range(T):
    n = int(input())
    half = n // 2

    for i in range(half, 1, -1):
        if (half in isprime_list) and ((n-half) in isprime_list): # half와 n-half가 리스트에 있는지 확인하기.
            print(half, (n-half))
            break
        half -= 1