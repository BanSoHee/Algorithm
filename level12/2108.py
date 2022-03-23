## 정렬 - 통계학

from cmath import inf

list_num = []
n = int(input()) # 홀수임.

for i in range(n):
    num = int(input())
    list_num.append(num)

# 오름차순으로 정렬.
list_num_up = sorted(list_num)
# 중복 수 제거.
list_num_set = list(set(list_num))

# 산술 평균.
print(round(sum(list_num) / n))
# 중앙값.
print(list_num_up[int(n/2)])
# 최빈값. => 내일 수정. 여러 개 있을 경우 최빈값 중 두 번재로 작은 값 출력.
first = -inf
second = -inf
for i in list_num_set:
    num_count = list_num_set.count(i)
    if num_count > first:
        first_num = i
        first = num_count
    elif num_count <= first and num_count >= second:
        second_num = i
        second = num_count
print(second_num)
# 범위.
print(max(list_num) - min(list_num))