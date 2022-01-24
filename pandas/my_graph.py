import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
football = pd.read_csv("data_sf.csv")


# ФУНКЦИЯ СОЗДАНИЯ ГРАФА СВЯЗЕЙ ОБЪЕКТОВ
def graph_links():
    plt.title('Моя схема связей')
    g = nx.Graph()
    n1 = 'Дмитрий Пилипенко'
    n2 = 'Ольга Пилипенко'
    n3 = 'Елена Пилипенко'
    g.add_nodes_from([n1, n2, n3])
    g.add_edges_from([(n1, n2), (n1, n3)])
    nx.draw(g, with_labels=True)


# ФУНКЦИЯ СОЗДАНИЯ ГРАФА ЕЖЕДНЕВНЫХ ЗНАЧЕНИЙ
def graph_daily_statistic():
    plt.title('Статистика заполнения таблицы')
    days = ['26.01', '27.01', '28.01']
    records = [0, 0, 9]
    plt.plot(days, records)


#  ФУНКЦИЯ СОЗДАНИЯ ГРАФА ФУТБОЛЬНОЙ СТАТИСТИКИ
def graph_football():
    plt.title('Футбольная статистика')
    name = football['Name'].head(10)
    result = football['Age'].head(10)
    plt.plot(name, result)


# ФУНКЦИЯ ЭКСПЕРИМЕНТОВ PANDAS
def football_anal():
    result = football[['Name', 'Age']].head(10)
    return result


# ВЫВОД РЕЗУЛЬТАТА ЭКСПЕРИМЕНТОВ С PANDAS
print(football_anal())

# ВЫБОР ГРАФА И ВЫВОД ЕГО НА ЭКРАН C СОХРАНЕНИЕМ В ФАЙЛ

# graph_links()  # ВЫБОР ГРАФА СВЯЗЕЙ
# graph_daily_statistic()  # ВЫБОР ГРАФА ЕЖЕДНЕВНЫХ ЗНАЧЕНИЙ
graph_football()
plt.savefig('mpl_out.png')  # сохраняем график
plt.show()  # show graph

