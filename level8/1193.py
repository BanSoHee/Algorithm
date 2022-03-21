## 기본 수학1 - 분수찾기

n = int(input()) # 몇 번째 분수를 찾을 것인가.

# 몇 번째 층인지를 찾기.
val = 0; count = 1
while True:
    val += count; #print('val:', val, 'count:', count)
    if val >= n:
        #print('result count:', count)
        break
    count += 1

# 몇 번째 호인지를 찾기.
linenum = n - (val - count)
#print('linenum:', linenum)

# 짝수층(분모 층으로 시작)인지 홀수층(분모 1로 시작)인지 찾기.
# 짝수층 이라면.
if count % 2 == 0:
    up = linenum
    down = count + 1 - up
else:
    down = linenum
    up = count + 1 - linenum

print(str(up) + '/' + str(down))