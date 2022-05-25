try:
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))

    print("Результат деления:", number_1 / number_2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение")
