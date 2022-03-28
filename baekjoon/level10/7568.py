## 브루트 포스 - 덩치

# 덩치 = (x, y) = (몸무게, 키)
wh = []
n = int(input())

# [(w1, h1), ... , (wn, hn)]
for i in range(n):
    w, h = map(int, input().split())
    wh.append((w, h))

# 굳이 오름, 내림차순으로 정렬할 필요 없이 앞에 몇 사람이 있는지를 판단하면 됨.
for i in range(n):
    count = 1
    for j in range(n):
        if wh[j][0] > wh[i][0] and wh[j][1] > wh[i][1]:
            count += 1
    print(count, end=' ')