my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0 #  Начальный индекс
while i < len(my_list): # Начинаем цикл
    zero = my_list[i] # Создаем переменную
    if zero > 0: # Проверяем числа больше нуля
        print(zero)
    elif zero < 0: # Проверяем числа меньше нуля
        break
        print(zero)
    else: # Если элемент равен нулю, пропускаем
        i += 1
        continue
        print(zero)
    i += 1 # Переходим по элементу

