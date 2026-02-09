import math


def square(side):
    return math.ceil(side * side)


side_lenght = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата = {square(side_lenght)}")
