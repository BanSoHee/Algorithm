## 함수 - 4673번

target = 10000

# d(n) = n + (n의 각 자리수의 합)
def d(n):
    sum = 0

    # n + (n의 각 자리수의 합) 수행.
    for i in range(len(str(n))):
        sum = sum + int(str(n)[i])
    result = n + sum

    # 해당 자리 값 바꿈.
    if result > target:
        return
    list[result - 1] = 1
    #print(result)
    #time.sleep(1)

    return d(result)


def main():

    # 100보다 작은 셀프 넘버가 들어갈 리스트 생성.
    global list
    list = []
    for i in range(target):
        list.append(0)

    # 셀프 넘버 여부 확인.
    for i in range(1, target + 1):
        d(i)

main()

for i in range(target):
    if list[i] == 0:
        print(i+1)
