## 기본 수학1 - 2292번

# 벌집의 개수가 6, 12, 18, 24, ... 개씩 증가.

n = int(input())

bee_count = 1  # 벌집의 개수, 1개부터 시작
cnt = 1

while n > bee_count :
    bee_count += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수

print(cnt)