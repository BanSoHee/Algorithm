## 기본 수학 2 - 3009번

a, b = input().split()
c, d = input().split()
e, f = input().split()

if a == c:
    x = e
    if b == d:
        y = f
    elif b == f:
        y = d
    else:
        y = b
elif a == e:
    x = c
    if b == d:
        y = f
    elif b == f:
        y = d
    else:
        y = b
else:
    x = a
    if b == d:
        y = f
    elif b == f:
        y = d
    else:
        y = b
print(x, y)