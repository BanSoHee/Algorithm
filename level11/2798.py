## 브루트 포스 - 블랙잭

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
max = 0

# num_list에 있는 수들의 합(3개합) 중 m보다 작으면서 m과 가장 가까운 세 수 출력하기.
for i in num_list:
    for j in num_list:
        for k in num_list:
            if i != j and i != k and j != k:
                sum = i + j + k
                if sum <= m and sum > max:
                    max = sum
                    a, b, c = i, j, k

print(a + b + c)