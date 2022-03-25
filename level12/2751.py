## 정렬 - 수 정렬하기 2

import sys

list_num = []
n = int(input())

for i in range(n):
    list_num.append(int(sys.stdin.readline()))

for i in sorted(list_num):
    sys.stdout.write(str(i) + '\n')