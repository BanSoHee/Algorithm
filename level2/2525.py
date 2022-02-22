## if문 - 2525번

# 현재 시간 (시, 분)
time = input()
h = int(time.split()[0])
m = int(time.split()[1])

# 조리 시간 (분)
c = int(input())
c_h = c // 60       # 조리 시간 (시)
c_m = c - c_h * 60  # 조리 시간 (분)

# 오븐 구이 끝나는 시간
if m + c_m < 60: 
    result_m = m + c_m
    if h + c_h < 24:
        result_h = h + c_h
    result_h = (h + c_h) % 24
else:
    result_m = (m + c_m) % 60
    wait_h = (m + c_m) // 60
    if h + c_h + wait_h < 24:
        result_h = h + c_h + wait_h
    result_h = (h + c_h + wait_h) % 24

# result
print(result_h, result_m)