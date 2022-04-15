## 정렬 - 나이순 정렬

import sys

old = ['name'] * 201 # 나이: 1 ~ 200.
n = int(input())

for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    if old[age] == 'name':
        old[age] = [name]
    else:
        old[age].append(name)
for i in range(len(old)):
    if old[i] != 'name':
        for j in old[i]:
            print(i, j)