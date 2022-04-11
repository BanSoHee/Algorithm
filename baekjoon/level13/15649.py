## 백트래킹 - N과 M(1)

import sys

n, m = map(int, sys.stdin.readline().split())

# 1 ~ N 수 중 중복없이 M개를 고른 수열.
s = []
def dfs():
    global s
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()