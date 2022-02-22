## 문자열 - 1157번

""" ----------------------------------------------
=> 시간 초과 됨.

string = input()
string = string.upper() # 모두 대문자로 바꿈.

max = 0
result = ""
for i in range(len(string)):
    count_num = string.count(string[i])
    if count_num > max:
        max = count_num
        result = string[i]

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우 확인.
count = 0
for i in range(len(string)):
    if max == string.count(string[i]):
        count += 1

if count != max:
    result = "?"

print(result)
---------------------------------------------- """ 


""" ----------------------------------------------
=> 시간 초과 됨. => string 의 길이가 길어지면 시간 초과 발생할 수도 있을 듯....?  => 알파벳으로 접근해볼까.
string = input()
string = string.upper() # 모두 대문자로 바꿈.

list = []

for i in range(len(string)):
    list.append(string.count(string[i]))

if max(list) == list.count(max(list)):
    print(string[list.index(max(list))])
else:
    print("?")
---------------------------------------------- """

string = input()
string = string.upper() # 모두 대문자로 바꿈.

# 알파벳 list 생성
alphabet = list(range(97, 123)) # 알파벳의 아스키코드 숫자 범위 97 - 122.

for i in alphabet:
    alphabet[i-97] = string.count(chr(i).upper()) # 아스키코드 -> A-Z count.

if alphabet.count(max(alphabet)) > 1:
    print("?")
else:
    print(chr(alphabet.index(max(alphabet)) + 97).upper())