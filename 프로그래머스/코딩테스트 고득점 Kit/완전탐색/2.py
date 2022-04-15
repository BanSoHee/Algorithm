## 완전탐색 - 소수 찾기(isprime func, permutations 이용)

## 소수 판별 func.
def isprime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

## 탐색 func.
from itertools import permutations

def solution(numbers):
    count = 0
    total_l = []

    for i in range(1, len(numbers)+1):
        l = list(map(''.join, permutations(list(numbers), i)))
        total_l += l

    for i in list(set(list(map(int, total_l)))):
        if isprime(i):
            count += 1
            
    return count

print(solution("011"))