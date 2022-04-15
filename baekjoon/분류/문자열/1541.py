## 문자열 - 잃어버린 괄호

# 괄호를 적절히 쳐서 식의 값을 최소로 만드는 프로그램.
# 1) '0' ~ '9', '+', '-' 만 존재.
# 2) 가장 처음과 마지막 문자는 숫자
# 3) 두 개 이상의 연산자가 나타나지는 않음.

import sys
def sol(inputval):
    l = list(inputval)
    print(l)

    # 모든 연산자가 같다면 그대로 return.
    # '-' 뒤에서 괄호 시작. '+' 숫자 앞 괄호 닫기.
    if '+' in l and '-' not in l:
        return int(inputval)

#val = sys.stdin.readline().strip()
val = '55-50+40' # => test value.
sol(val)