## 재귀 - 하노이 탑 이동 순서

# 원판 이동 과정 출력 함수.
def move(n, start, end):

    # 원판 하나.
    if n == 1:
        print(start, end)
        return
    
    # 원판 여러 개.
    move(n-1, start, 6-start-end)
    print(start, end)
    move(n-1, 6-start-end, end)

N = int(input()) # 원판 수 입력받기.
print(N**2 - 1)  # 원판 이동 횟수 출력.
move(N, 1, 3)          # 원판 이동 과정 출력.