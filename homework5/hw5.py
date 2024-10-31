def main():
    total_sum = 0  # Переменная для хранения суммы
    while True:  # Бесконечный цикл
        user_input = input("Введите число (или 'stop end' для завершения): ")
        
        # Проверяем на команду завершения
        if user_input.lower() == 'stop end':
            break
        
        try:
            number = float(user_input)  # Пробуем преобразовать ввод в число
            total_sum += number  # Добавляем число к общей сумме
        except ValueError:
            print("Пожалуйста, введите корректное число.")  # Обработка некорректного ввода

    print(f"Сумма введенных чисел: {total_sum}")  # Вывод суммы

if __name__ == "__main__":
    main()