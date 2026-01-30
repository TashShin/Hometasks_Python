# округление стороны (переданного аргумента) до высшего
import math


def square(side):
    return side * side


num_side = math.ceil(float(input("Введите число: ")))
print(f"Площадь квадрата равна: {square(num_side)}")
