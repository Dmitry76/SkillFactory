import matplotlib.pyplot as plt
import pandas as pd


# ВЫБОР ИСТОЧНИКА ДАННЫХ
football = pd.read_csv("data_sf.csv")

# ОБЪЕДИНЕНИЕ ТАБЛИЦ


# ВЫБОРКА СТОЛБЦОВ
x = football[football.Nationality == 'Portugal'].loc[:, ['Name', 'Age']].head()
print(x)


# ГРУППИРОВКА ДАННЫХ И ПРИМЕНЕНИЕ АНАЛИТИКИ
r = football[football.Wage > football.Wage.mean()].Nationality.value_counts().loc[lambda x1: x1 > 50]
s = football[football.Value > football.Value.mean()].Nationality.value_counts().loc[lambda x1: x1 > 50]
print('===========')
print(r, s)
print('===========')
print(football[football.Age > 35].Wage)  # выводим колонку Wage записей, где Age больше 20
print(football[football.Age > football.Age.mean()])  # записи таблицы, где Age выше среднего

# ОТРИСОВКА ГРАФОВ
plt.plot(r)
plt.plot(s)
plt.savefig('mpl_out.png')  # сохраняем график
plt.show()  # show graph

