## if문 - 2480번

num123 = input()
num1 = int(num123.split()[0])
num2 = int(num123.split()[1])
num3 = int(num123.split()[2])

# 3개 모두 같을 경우.
if num1 == num2 == num3:
    result = 10000 + num1 * 1000
# 3개 모두 다를 경우.
elif num1 != num2 and num2 != num3 and num1 != num3:
    result = max(num1, num2, num3) * 100
# 2개만 같을 경우.
else:
    if num1 == num2:
        result = 1000 + num1 * 100
    elif num1 == num3:
        result = 1000 + num1 * 100
    elif num2 == num3:
        result = 1000 + num2 * 100

print(result)