## 해시 - 위장

def solution(clothes):
    # [[의상이름1, 의상종류1], ...]
    clo_dic = {i[1]:0 for i in clothes} # 옷장 딕셔너리 선언.

    for i in clothes:
        clo_dic[i[1]] += 1
    
    sum = 1
    if len(list(clo_dic.values())) == 1:
        return len(clothes)
    else: ## 여러 개의 옷 종류가 있을 경우가 에러남. 고치기.
        for i in list(clo_dic.values()):
            sum *= i
        return len(clothes) + sum

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))