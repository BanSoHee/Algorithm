## 해시 - H-Index

def solution(citations):
    # 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용.
    # => 이때의 h의 최댓값.
    # H-Index = h.
    citations.sort() # 오름차순 정렬.
    for i in range(len(citations)):
        if citations[i] == len(citations)-i:
            return len(citations)-i
    return 0

print(solution([3, 0, 6, 1, 5]))