## 해시 - 전화번호 목록

def solution(phone_book):
    # phone_book = 전화번호를 담은 배열.
    # 접두사 확인.
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
        #phone_book[i+1] = phone_book[i+1].replace(phone_book[i], '*')
        #if phone_book[i+1][0] == '*':
            return False
    return True