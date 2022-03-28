## 정렬 - 좌표 압축

import sys

n = int(sys.stdin.readline().strip())
xlist = list(map(int, sys.stdin.readline().strip().split()))
set_xlist = sorted(list(set(xlist))) # 인덱스 = 해당 숫자보다 작은 수 개수.

dic = {set_xlist[i]:i for i in range(len(set_xlist))} # => 시간 복잡도 O(1)

for i in xlist:
    # print(len([k for k in set_xlist if i > k]), end=' ') => 매번 최대 1,000,000번 수행이 이루어짐.
    print(dic[i], end=' ')