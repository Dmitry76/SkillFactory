import numpy as np

#  ПЕРЕМЕННЫЕ
count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
predict_max = 100  # максимум загаданного интервала
predict_min = 1  # минимум загаданного интервала

#  ФУНКЦИИ
def predict(pr_min, pr_max):  #  РАСЧЕТ ПРЕДПОЛАГАЕМОГО ЧИСЛА
    """Функция расчитывает подходящее предполагаемое число,
    исходя из известных минимума и максимума интервала"""
    result = predict_min + (predict_max - predict_min) // 2  # формула расчета предполагаемого числа
    return result


#  РАБОЧАЯ ОБЛАСТЬ
while True:  # бесконечный цикл
    predict_number = int(predict(predict_min, predict_max))  # расчитываем предполагаемое число
    print(f'Пробуем {predict_number}')  # выводим предполагаемое число в консоль
    count += 1  # плюсуем попытку
    if number == predict_number:
        break  # выход из цикла, если угадали
    elif number > predict_number:
        print(f"Угадываемое число больше {predict_number} ")
        predict_min = predict_number  # меняем минимум загаданного интервала
    elif number < predict_number:
        print(f"Угадываемое число меньше {predict_number} ")
        predict_max = predict_number  # меняем максимум загаданного интервала

print(f"Вы угадали число {number} за {count} попыток.")
