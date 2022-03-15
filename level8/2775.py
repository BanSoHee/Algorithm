## 기본 수학1 - 부녀회장이 될테야

count = int(input()) # loop 횟수.

for i in range(count):

    # k층 n호 입력받기.
    k = int(input()) # 층
    n = int(input()) # 호

    # 0층 사람 수 list.
    floor0 = [i for i in range(1, 15)]

    # list 층에 따라서 변경하기.
    for i in range(k):
        for j in range(1, n):
            floor0[j] += floor0[j-1]
            #print(floor0)

    print(floor0[n-1])