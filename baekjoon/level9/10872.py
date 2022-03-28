## 재귀 - 팩토리얼

num = int(input())

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(num))