## 기본 수학 2 - 1002번

import math
num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # 두 원이 정확히 일치할 경우
    if dist == 0 and r1 == r2:
        print(-1)
    # 내접, 외접
    elif dist == abs(r1 - r2) or dist == r1 + r2:
        print(1)
    # 교점이 두 개일 경우
    elif abs(r1 - r2) < dist < r1 + r2:
        print(2)
    else:
        print(0)