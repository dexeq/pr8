def print_integers_between(a, b):
    # Определяем границы
    start = min(a, b) + 1  # Начинаем с числа, следующего за меньшим из a и b
    end = max(a, b)        # Заканчиваем на большем из a и b

    # Выводим числа между a и b
    for num in range(start, end):
        print(num)

# Запрашиваем ввод у пользователя
try:
    a = int(input("Введите первое число (a): "))
    b = int(input("Введите второе число (b): "))
    print(f"Целые числа между {a} и {b}:")
    print_integers_between(a, b)
except ValueError:
    print("Пожалуйста, введите корректные целые числа.")