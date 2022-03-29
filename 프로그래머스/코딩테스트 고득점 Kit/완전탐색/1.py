## 완전탐색 - 모의고사

def solution(answers):
    qlen = len(answers)

    one = []; two = []; three = []
    count1, count2, count3 = 0, 0, 0
    one_list = [1, 2, 3, 4, 5]
    two_list = [2, 1, 2, 3, 2, 4, 2, 5]
    three_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(qlen):
        one.append(one_list[i%5])
        two.append(two_list[i%8])
        three.append(three_list[i%10])

    for i in range(qlen):
        if answers[i] == one[i]:
            count1 += 1
        if answers[i] == two[i]:
            count2 += 1
        if answers[i] == three[i]:
            count3 += 1
        
    correct = [count1, count2, count3]
    maxcorrect = max([count1, count2, count3])
    if correct.count(maxcorrect) == 1:
        return [correct.index(maxcorrect) + 1]
    else:
        sol = []
        for i in range(3):
            if correct[i] == maxcorrect:
                sol.append(i+1)
    return sol

print(solution([1,3,2,4,2]))