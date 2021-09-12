import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
predict_max = 100  # максимум загаданного интервала
predict_min = 1  # минимум загаданного интервала

while True:  # бесконечный цикл
    predict = predict_min+(predict_max - predict_min)//2  # расчитываем предполагаемое число
    print(f'Пробуем {predict}')  # выводим предполагаемое число в консоль
    count += 1  # плюсуем попытку
    if number == predict:
        break  # выход из цикла, если угадали
    elif number > predict:
        print(f"Угадываемое число больше {predict} ")
        predict_min = predict  # меняем минимум загаданного интервала
    elif number < predict:
        print(f"Угадываемое число меньше {predict} ")
        predict_max = predict  # меняем максимум загаданного интервала

print(f"Вы угадали число {number} за {count} попыток.")
