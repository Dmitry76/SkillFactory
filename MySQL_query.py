import getpass


# ФУНКЦИИ
# ВЫВОД СПИСКА БД
def show_databases(host, user, password):

    from mysql.connector import connect, Error
    try:
        with connect(
                host=host,
                user=user,
                password=password,
        ) as connection:
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute("show databases")
                print("===========================================================================================")
                for row in cursor:
                    for field in row:
                        print(str(field))
                    # connection.close()
                print("===========================================================================================")
                return True
    except Error as e:
        print(e)

        # connection.close()
        return False
# ===================================


# ВЫВОД СПИСКА ТАБЛИЦ
def show_tables(host, user, password, database):

    from mysql.connector import connect, Error
    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database=database,
        ) as connection:
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute("show tables")
                print("===========================================================================================")
                for row in cursor:
                    for field in row:
                        print(str(field))
                    # connection.close()
                print("===========================================================================================")
                return True
    except Error as e:
        print(e)

        # connection.close()
        return False
# ===================================


# ВЫВОД СПИСКА ПОЛЕЙ ТАБЛИЦЫ
def show_fields(host, user, password, database, table_name):

    from mysql.connector import connect, Error
    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database=database,
        ) as connection:
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute(f"show columns from {table_name}")
                print("===========================================================================================")
                for row in cursor:
                    print(row[0])
                # connection.close()
                print("===========================================================================================")
                return True
    except Error as e:
        print(e)
        print("===========================================================================================")
        # connection.close()
        return False
# ===================================


# ОБРАБОТКА ЗАПРОСА
def query_execute(host, user, password, database, my_query):

    from mysql.connector import connect, Error
    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database=database,
        ) as connection:
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute(my_query)
                print("===========================================================================================")
                for row in cursor:
                    for field in row:
                        print(str(field))
                    print("===========================================================================================")
                    # connection.close()
    except Error as e:
        print(e)
        # connection.close()
# ===================================


# СТАРТУЕМ, ВВОД ХОСТА И ИМЯ БД
host_adr = input("Host: ")
host_user = input("Пользователь: ")
host_pass = getpass.getpass()
print("Список доступных БД:")
if show_databases(host_adr, host_user, host_pass):
    bd_name = input("Имя БД: ")
else:
    host_adr = '---'
    bd_name = '---'
# МЕНЮ СЕРВИСА
while True:
    print(f"=========================\n"
          f"Host: {host_adr}\n"
          f"Имя БД: {bd_name}"
          f"\n=========================\n"
          "1 - Изменить Хост и БД\n"
          "2 - Изменить БД\n"
          "3 - Новая выборка SELECT FROM WHERE\n"
          "0 - Выход"
          "\n=========================")
    action = input("Ваш выбор: ")

    if action == "1":
        host_adr = input("Host: ")
        host_user = input("Пользователь: ")
        host_pass = getpass.getpass()
        print("Список доступных БД:")
        if show_databases(host_adr, host_user, host_pass):
            bd_name = input("Имя БД: ")
        else:
            host_adr = '---'
            bd_name = '---'

    elif action == "2" and host_adr != '---':
        print("Список доступных БД:")
        if show_databases(host_adr, host_user, host_pass):
            bd_name = input("Имя БД: ")
        else:
            bd_name = '---'

    elif action == "3":
        print("Список доступных таблиц БД:")
        if show_tables(host_adr, host_user, host_pass, bd_name):
            tab_name = input("Имя таблицы: ")
            print(f"Список полей таблицы {tab_name}:")
            if show_fields(host_adr, host_user, host_pass, bd_name, tab_name):
                fields = input("Поля для вывода: ")
                query = input("Ваш запрос: ")
                query_execute(host_adr, host_user, host_pass, bd_name,
                              f"select {fields} from {tab_name} where {query}")

        else:
            bd_name = '---'

    elif action == "0":
        print("Удачной охоты!")
        break
