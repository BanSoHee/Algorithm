## 기본 수학1 - ACM 호텔

## 반복 횟수.
count = int(input())

for i in range(count):
    ## 층, 호, 몇 번째 손님인지.
    H, W, N = map(int, input().split())

    floor = N % H                    # 몇 층에 배정될 지.
    roomnum = ((N+H) - floor) // H   # 몇 호에 배정될 지.

    # floor == 0일 경우.
    if N % H == 0:
        floor = H
        roomnum = ((N+H) - floor) // H
        
    if len(str(roomnum)) == 1: result_roomnum = '0' + str(roomnum)
    else: result_roomnum = str(roomnum)

    result = str(floor) + result_roomnum
    print(result)