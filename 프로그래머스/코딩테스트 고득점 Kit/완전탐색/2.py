## 완전탐색 - 소수 찾기 =============> 이거 다시.

# 소수 판별 func.
def isprime(n):
    if n == 0: return False
    if n == 1: return False
    if n == 2: return True
    for i in (2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

"""
# dfs func.
s = []
count = 0

def dfs():
    global l, s, count

    if len(s) == 0:
        pass
    elif isprime(int(''.join(s))):
        print(int(''.join(s))) # <------------- 숫자 확인. 왜 71 없을....까.....ㅠㅠㅠㅠㅠㅠ
        count += 1
        return

    for i in l:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

def solution(numbers):
    global l
    l = list(numbers)
    dfs()
    return count
"""
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