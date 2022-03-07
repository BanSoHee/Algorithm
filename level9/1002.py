## 기본 수학 2 - 1002번

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        print(0)
    elif r1 + r2 > ((x1 - x2)**2 + (y1 - y2)**2)**(1/2):
        print(2)
    elif r1 + r2 == ((x1 - x2)**2 + (y1 - y2)**2)**(1/2):
        print(1)
    else:
        print(0)