## 정렬 - 좌표 정렬하기

import sys

l = []
n = int(input())
for i in range(n):
    xy = str(sys.stdin.readline())
    x, y = map(int, xy.split())
    l.append((x, y))

l.sort()
for i in l:
    print(i[0], i[1])