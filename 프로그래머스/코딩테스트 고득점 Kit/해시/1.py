## 해시 - 완주하지 못한 선수

def solution(participant, completion): 
    # participant = 마라톤 선수들의 이름이 담긴 배열.
    # completion = 완주한 선수들의 이름이 담긴 배열.
    # return => 완주하지 못한 선수의 이름.
    dic = {i:0 for i in list(set(participant))}
    for i in participant:
        dic[i] += 1

    for i in completion:
        dic[i] -= 1

    answer_dic = dict(map(reversed, dic.items())) # 딕셔너리 value 값으로 key 찾기.
    answer = answer_dic[1]

    return answer