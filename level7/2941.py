## 문자열 - 2941번

croword = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()
for i in croword:
    str = str.replace(i, "*")

print(len(str))