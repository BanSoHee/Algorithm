## 정렬 - 소트인사이드

import sys

n = list(str(sys.stdin.readline()))
n.sort(reverse=True)
for i in range(len(n)-1):
    print(n[i], end='')