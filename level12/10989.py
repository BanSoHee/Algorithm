## 정렬 - 수 정렬하기 3 => 내일.

list_num = []
n = int(input())

for i in range(n):
    num = int(input())
    list_num.append(num)

list_num.sort()
for i in range(n):
    print(list_num[i])