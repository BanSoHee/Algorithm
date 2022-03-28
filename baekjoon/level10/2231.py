## 브루트 포스 - 분해합

N = int(input())

## 각 숫자의 분해합 계산하기. (1 ~ 1000000)
num_sum_list = [0] # 0은 0, 각 인덱스 숫자에 해당하는 분해합 append.
for i in range(1, N):
    num_sum = i + sum(map(int, list(str(i)))) # 숫자 + 각 자리수의 합
    num_sum_list.append(num_sum)

try:
    print(num_sum_list.index(N))
except:
    print(0)