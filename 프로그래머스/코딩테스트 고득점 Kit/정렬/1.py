## 정렬 - K 번째 수

def solution(array, commands):
    # array = 입력된 배열.
    # commands = [i, j, k]
    answer = []

    for co in commands:
        i, j, k = co
        answer.append(sorted(array[i-1:j])[k-1])

    return answer

#print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))