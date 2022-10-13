import math

print("1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 5 - вычисление корней квадратного уравнения")
number = int(input("Введите число от 1 до 5: "))

spisok = []
spisok = number

a = int(input("Введите a:  "))
b = int(input("Введите b:  "))

if spisok == 1:
    def sum(a, b):
        result = a + b
        return result


    print("Результат сложения:", sum(a, b))

if spisok == 2:
    def minus(a, b):
        result = a - b
        return result


    print("Результат вычитания:", sum(a, b))

if spisok == 3:
    def prois(a, b):
        result = a * b
        return result


    print("Результат умножения:", sum(a, b))

if spisok == 4:
    def dell(a, b):
        result = a / b
        return result


    print("Результат деления:", sum(a, b))

if spisok == 5:
    f = 2 * a  # знаменатель дроби при вычислении x
    c = int(input("Введите c: "))

    def discriminant(a,b,c):
        d = int((b ** 2) - 4 * a * c)  # дискриминат
        return d
    if discriminant(a,b,c) < 0:
        print("корней нет")
    else:
        if discriminant(a,b,c) == 0:
            x1 = -b / f
            print("x = " + str(x1))
        else:
            x1 = ((-b) + (discriminant(a,b,c) ** 0.5)) / f
            x2 = ((-b) - (discriminant(a,b,c) ** 0.5)) / f
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
