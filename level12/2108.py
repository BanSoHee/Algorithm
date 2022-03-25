## 정렬 - 통계학

import sys

list_num = []
n = int(input())

# plus_list = [0] * 4001
# minus_list = [0] * 4001

for i in range(n):
    num = int(sys.stdin.readline())
    list_num.append(num)
    # if num >= 0:
    #     plus_list[num] += 1
    # else:
    #     minus_list[num] += 1

# 산술평균.
print(round(sum(list_num) / n))

# 중앙값. (단, 입력한 개수는 홀수개임.)
list_num.sort()
print(list_num[int(n//2)])

# 최빈값.
# p_m_list = plus_list + minus_list
# max_count = max(p_m_list)
# max_nums = []
# if p_m_list.count(max_count) == 1:
#     if p_m_list.index(max_count) <= 4000:
#         print(plus_list.index(max_count))
#     else:
#         print(minus_list.index(max_count) - 4001)
# else:
#     for i in range(4001):
#         if plus_list[i] == max_count:
#             max_nums.append(i)
#         if minus_list[i] == max_count:
#             max_nums.append(i-4001)
#     max_nums.pop(min(max_nums))
#     print(min(max_nums))


from collections import Counter

count_nums = Counter(list_num).most_common()
if len(count_nums) > 1:
    if count_nums[0][1] == count_nums[1][1]:
        print(count_nums[1][0])
    else:
        print(count_nums[0][0])
else:
    print(count_nums[0][0])


# 최댓값과 최솟값의 차이.
print(max(list_num) - min(list_num))