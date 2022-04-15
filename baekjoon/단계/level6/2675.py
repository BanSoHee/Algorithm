## 문자열 - 2675번

count = int(input()) # 반복 횟수.
for i in range(count):
    result = ""

    numstring = input()
    num = int(numstring.split()[0])
    string = numstring.split()[1]

    for i in range(len(string)):
        result = result + num * string[i]
        
    print(result)