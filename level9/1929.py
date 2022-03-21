## 기본 수학2 - 소수 구하기

M, N = map(int, input().split())

## M 이상 N 이하의 소수 구하기. (소수가 하나 이상 있는 입력만 주어짐.) => 시간초과
# for i in range(M, N+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else: print(i)

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)
