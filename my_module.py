""" Этот модуль является сборником функций разработанных
    в качестве домашних заданий в курсе Python Basic"""

__all__ = ["visioner_array",
           "visioner_list",
           "adder_columns",
           "sorter_last_raw",
           "sorter_columns_up",
           "sorter_columns_down",
           "sorter_bubble",
           "sorter_by_insert",
           "sorter_selection"
           ]


def visioner_array(arr):
    """
    Функция выводит на печать квадратную матрицу
    :param arr: матрица
    :return:
    """
    for el in arr:
        for col in el:
            print(f'{col:^6}', end='')
        print()
    print()


def visioner_list(my_list: list) -> None:
    """
    Функция выводит на печать список
    :param my_list: список
    :return:
    """
    for el in my_list:
        print(f'{el:^6}', end='')
    print()
    print()


def adder_columns(m_x_m: list) -> list:
    """ Функция считает сумму столбцов матрицы"""
    m = len(m_x_m)
    m_list = [0 for _ in range(m)]
    for column_ in range(m):
        for raw_ in range(m):
            m_list[column_] += m_x_m[raw_][column_]
    # m_x_m.append(m_list)
    return m_list


def sorter_last_raw(m_x_m: list) -> list:
    """Сортирует столбцы по последнему ряду матрицы"""
    m = len(m_x_m) - 1
    for j in range(m):
        for i in range(m):
            if m_x_m[m][i] > m_x_m[m][i + 1]:
                m_x_m[m][i], m_x_m[m][i + 1] = m_x_m[m][i + 1], m_x_m[m][i]
                for __ in range(m):
                    m_x_m[__][i], m_x_m[__][i + 1] = m_x_m[__][i + 1], \
                        m_x_m[__][i]
    return m_x_m


def sorter_columns_up(m_x_m: list) -> list:
    """Сортирует столбец снизу вверх"""
    m = len(m_x_m)
    for __ in range(m):
        for j in range(m - 1):
            for i in range(m):
                if m_x_m[j][i] < m_x_m[j + 1][i]:
                    m_x_m[j][i], m_x_m[j + 1][i] = \
                        m_x_m[j + 1][i], m_x_m[j][i]
    return m_x_m


def sorter_columns_down(m_x_m: list) -> list:
    """Сортирует столбец сверху вниз"""
    m = len(m_x_m)
    for __ in range(m):
        for j in range(m - 1):
            for i in range(m):
                if m_x_m[j][i] > m_x_m[j + 1][i]:
                    m_x_m[j][i], m_x_m[j + 1][i] = \
                        m_x_m[j + 1][i], m_x_m[j][i]
    return m_x_m


def sorter_bubble(my_list: list) -> list:
    """Алгоритм пузырьковой сортировки"""
    m = len(my_list)
    for _ in range(m):
        for __ in range(m - 1):
            if my_list[__] > my_list[__ + 1]:
                my_list[__], my_list[__ + 1] = my_list[__ + 1], my_list[__]
    return my_list


def sorter_by_insert(my_list: list) -> list:
    """Алгоритм сортировки вставками"""
    m = len(my_list)
    for i in range(m):
        cursor = my_list[i]
        pos = i
        while pos > 0 and my_list[pos - 1] > cursor:
            my_list[pos] = my_list[pos - 1]
            pos -= 1
        my_list[pos] = cursor
    return my_list


def sorter_selection(my_list: list) -> list:
    """Алгоритм сортировки выбором"""
    m = len(my_list)
    for i in range(m):
        min_ = i
        for j in range(i + 1, m):
            if my_list[j] < my_list[min_]:
                min_ = j
        my_list[min_], my_list[i] = my_list[i], my_list[min_]
    return my_list


# if __name__ == "__main__":
    # проверка фунций на работоспособность
    # r = 7
    #
    # m_na_m = [[rnd.randint(1, 99) for _ in range(r)] for __ in range(r)]
    # visioner_array(m_na_m)
    #
    # visioner_list(adder_columns(m_na_m))
    #
    # sorter_last_raw(m_na_m)
    # visioner_array(m_na_m)
    #
    # sorter_columns_up(m_na_m)
    # visioner_array(m_na_m)
    #
    # sorter_columns_down(m_na_m)
    # visioner_array(m_na_m)
    #
    # m_listik = [rnd.randint(1, 199) for _ in range(11)]
    # visioner_list(m_listik)
    # visioner_list(sorter_selection(m_listik))
