## 기본 수학2 - 택시 기하학

from cmath import pi


R = int(input())

## 유클리드 기하학에서의 원의 넓이.
print(R * R * pi)

## 택시 기하학에서의 원의 넓이.
## 거리가 R인 점들의 집합.
print(2 * (R**2))