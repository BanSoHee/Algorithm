## 정렬 - 좌표 정렬하기 2

import sys

l = []
n = int(input())
for i in range(n):
    x, y = map(int, str(sys.stdin.readline()).split())
    l.append((y, x))

l.sort()
for i in l:
    print(i[1], i[0])