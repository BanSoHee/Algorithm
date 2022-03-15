## 기본 수학2 - 소인수분해

n = int(input())

while True:
    if n == 1:
        break
    for i in range(2, n):
        if n % i == 0:
            print(i)
            n = int(n / i)
            break
    else:
        print(n)
        break