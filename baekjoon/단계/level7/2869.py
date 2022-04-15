## 기본 수학1 - 달팽이는 올라가고 싶다

A, B, V = map(int, input().split()) # 낮에 올라가는 길이, 밤에 내려가는 길이, 나무 높이.

## => 시간 초과.
# count = 0
# total_up = 0
# while True:

#     total_up += A # 낮에 올라감.
#     count += 1

#     if total_up >= V:
#         print(count)
#         break

#     total_up -= B # 밤에 내려감.

import math

result = (V - B) / (A - B) # 한 번 정상에 올라가면 이후 미끄러지지 않음. 
# V / (A - B)는 정상에 올라가도 밤에 미끄러지는 상황을 포함한다.
print(math.ceil(result)) # 올림 처리. 4.1일 = 5일 걸렸다고 해야 함.