import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
predict_max = 100
predict_min = 1

while True:  # бесконечный цикл
    predict = predict_min+(predict_max - predict_min)//2
    print(f'Пробуем {predict}')
    count += 1  # плюсуем попытку
    if number == predict:
        break  # выход из цикла, если угадали
    elif number > predict:
        print(f"Угадываемое число больше {predict} ")
        predict_min = predict
    elif number < predict:
        print(f"Угадываемое число меньше {predict} ")
        predict_max = predict

print(f"Вы угадали число {number} за {count} попыток.")