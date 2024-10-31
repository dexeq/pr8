while True:
    user_input1 = input("Введите первое целое число (или 'exit' для выхода): ")
    if user_input1.lower() == 'exit':
        print("Выход из программы.")
        break

    user_input2 = input("Введите второе целое число (или 'exit' для выхода): ")
    if user_input2.lower() == 'exit':
        print("Выход из программы.")
        break

    try:
        # Преобразуем ввод в целые числа
        num1 = int(user_input1)
        num2 = int(user_input2)

        # Вычисляем сумму
        total = num1 + num2

        # Выводим результат
        print(f"Сумма {num1} и {num2} равна {total}")

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целые числа.")