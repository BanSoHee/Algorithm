## 기본 수학1 - 1712번

a, b, c = map(int,input().split())

if b >= c:      # 가변비용이 노트북 가격보다 같거나 크면,
    print(-1)   # 손익분기점 없음.
else:
    print(int(a // (c - b)) + 1)