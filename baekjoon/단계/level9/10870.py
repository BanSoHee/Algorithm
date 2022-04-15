## 재귀 - 피보나치 수 5

# 피보나치 수는 0과 1로 시작함.
# 다음 수는 앞 두 수의 합.

num = int(input())

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(num))