## 해시 - 위장

from itertools import combinations

def solution(clothes):
    # [[의상이름1, 의상종류1], ...]
    clo_dic = {i[1]:0 for i in clothes} # 옷장 딕셔너리 선언.
    for i in clothes:
        clo_dic[i[1]] += 1
    
    # 한 종류의 의상만 있을 경우.
    if len(clo_dic.values()) == 1:
        return len(clothes)
    
    # 여러 종류의 의상이 있을 경우.
    total_list = []
    sum = 1; resultsum = 0

    for i in range(2, len(list(clo_dic.values())) + 1): # 2 ~ len(의상 종류)개의 조합.
        total_list.append(list(combinations(list(clo_dic.values()), i)))

    for i in total_list:
        for j in i:
            for k in j:
                sum *= k
            resultsum += sum
            sum = 1

    return resultsum + len(clothes)

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))