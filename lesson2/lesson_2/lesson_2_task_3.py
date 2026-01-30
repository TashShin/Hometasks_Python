# округление площади до высшего
import math


def square(side):
    return math.ceil(side * side)


num_side = float(input("Введите число: "))

print(f"Площадь квадрата равна: {square(num_side)}")
