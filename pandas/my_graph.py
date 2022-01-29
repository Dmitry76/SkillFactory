import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
football = pd.read_csv("data_sf.csv")


# ФУНКЦИЯ СОЗДАНИЯ ГРАФА СВЯЗЕЙ ОБЪЕКТОВ
def graph_links(start):
    if start == 1:
        plt.title('Моя схема связей')
        g = nx.Graph()
        n1 = 'Дмитрий Пилипенко'
        n2 = 'Ольга Пилипенко'
        n3 = 'Елена Пилипенко'
        g.add_nodes_from([n1, n2, n3])
        g.add_edges_from([(n1, n2), (n1, n3)])
        nx.draw(g, with_labels=True)
    else:
        return


# ФУНКЦИЯ СОЗДАНИЯ ГРАФА ЕЖЕДНЕВНЫХ ЗНАЧЕНИЙ
def graph_daily_statistic(start):
    if start == 1:
        plt.title('Статистика заполнения таблицы')
        days = ['26.01', '27.01', '28.01']
        records = [0, 0, 9]
        plt.plot(days, records)
    else:
        return


#  ФУНКЦИЯ СОЗДАНИЯ ГРАФА ФУТБОЛЬНОЙ СТАТИСТИКИ
def graph_football(start):
    if start == 1:
        plt.title('Футбольная статистика')
        name = football['Name'].head(10)
        result = football['Age'].head(10)
        plt.plot(name, result)
    else:
        return


# ФУНКЦИЯ ЭКСПЕРИМЕНТОВ С PANDAS
def football_anal(start):
    if start == 1:
        result = football[['Name', 'Age']].head(10).max()
        return result
    else:
        result = ''
        return result


# СОХРАНЕНИЕ И ОТРИСОВКА ГРАФА
def run_plt(save, show):
    if save == 1:
        plt.savefig('mpl_out.png')
    elif show == 1:
        plt.show()
    else:
        return


# ВЫВОД РЕЗУЛЬТАТА ЭКСПЕРИМЕНТОВ С PANDAS
print(football_anal(1))

# ВЫБОР ГРАФА И ВЫВОД ЕГО НА ЭКРАН C СОХРАНЕНИЕМ В ФАЙЛ

graph_links(0)              # ВЫБОР ГРАФА СВЯЗЕЙ
graph_daily_statistic(0)    # ВЫБОР ГРАФА ЕЖЕДНЕВНЫХ ЗНАЧЕНИЙ
graph_football(0)           # ВЫБОР ГРАФА ФУТБОЛЬНОЙ СТАТИСТИКИ
run_plt(0, 0)               # СОХРАНЕНИЕ И ОТРИСОВКА ГРАФА

