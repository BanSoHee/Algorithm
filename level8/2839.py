## 기본 수학1 - 설탕 배달

N = int(input())

result = 0
while N >= 0:
    if N % 5 == 0:
        result = result + (N // 5)
        print(result)
        break
    N = N - 3
    result += 1
else: # while문이 거짓일 경우.
    print(-1)