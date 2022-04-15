## 백트래킹 - N과 M(2)

import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def dfs():
    global s

    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if len(s) == 0:
            pass
        elif s[-1] > i:
            continue

        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()    