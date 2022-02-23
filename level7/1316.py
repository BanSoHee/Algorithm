## 문자열 - 1316번

num = int(input())

error = 0
for i in range(num):
    str = input()
    for j in range(len(str)-1):
        if str[j] != str[j+1]:
            new_str = str[j+1:]
            if str[j] in new_str:
                error += 1
                break

print(num - error)