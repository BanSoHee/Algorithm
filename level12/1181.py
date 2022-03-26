## 정렬 - 단어 정렬

import sys

l = [0] * 51 # 문자열의 길이 1 - 50.
n = int(input())

for i in range(n):
    word = str(sys.stdin.readline().strip())
    if l[len(word)] == 0:
        l[len(word)] = [word]
    elif word in l[len(word)]:
        pass
    else:
        l[len(word)].append(word)

for i in l:
    if i == 0:
        pass
    else:
        i.sort()
        for j in i:
            print(j)