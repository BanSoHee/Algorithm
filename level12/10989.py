## 정렬 - 수 정렬하기 3

import sys

n = int(input())
num_list = [0] * 10001 # 1 ~ 10000 자연수.

for i in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)