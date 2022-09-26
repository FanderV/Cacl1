number = int(input())
print("Введите число от 1 до 5")
print("1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 5 - вычисление корней квадратного уравнения")


if number == 1:
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    result = (a+b)
    print("Результат сложения: " + str(result))

if number == 2:
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    result = (a - b)
    print("Результат вычитания: " + str(result))

if number == 3:
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    result = (a * b)
    print("Результат умножения: " + str(result))

if number == 4:
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    result = (a / b)
    print("Результат деления: " + str(result))

if number == 5:
    print("Введите a")
    a = int(input())
    print("Введите b")
    b = int(input())
    print("Введите c")
    c = int(input())
    d = int((b**2)-4*a*c) #дискриминат
    if d < 0:
        print("корней нет")
    else:
        f = 2 * a #знаменатель дроби при вычислении x
        if d == 0:
            x = -b/f
            print("x = " + str(x))
        else:
            f = 2 * a #знаменатель дроби при вычислении x
            x1 = ((-b)+(d**0.5))/f
            x2 = ((-b)-(d**0.5))/f
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))