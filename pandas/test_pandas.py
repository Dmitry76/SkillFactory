import matplotlib.pyplot as plt
import pandas as pd

football = pd.read_csv("data_sf.csv")

print(football[football.Age > 35].Wage)  # выводим колонку Wage записей, где Age больше 20
print(football[football.Age > football.Age.mean()])  # записи таблицы, где Age выше среднего

# отдельные поля выборки верхние 5 записей
x = football[football.Nationality == 'Portugal'].loc[:, ['Name', 'Age']].head()
print(x)

#  ВЫВОД ГРАФИКОВ
s = football[football.Value > football.Value.mean()].Nationality.value_counts().loc[lambda x1: x1 > 50]
r = football[football.Wage > football.Wage.mean()].Nationality.value_counts().loc[lambda x1: x1 > 50]
plt.plot(r)
plt.plot(s)
plt.savefig('mpl_out.png')  # сохраняем график
plt.show()  # show graph
