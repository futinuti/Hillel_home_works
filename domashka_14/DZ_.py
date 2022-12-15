import random as rnd


def visio_matrix(arr):
    """
    Функция выводит на печать квадратную матрицу
    :param arr: матрица
    :return:
    """

    for el in arr:
        for col in el:
            print(f'{col:^6}', end='')
        print()


def do_sorted_arr():
    """
    принимает размер и генерирует квадратную матрицу,
    функция вычисляет сумму столбцов
    и дописывает их снизу основной матрицы,
    сортирует столбцы матрицы по сумме этих столбцов
    сортирует сами столбцы по возрастанию снизу вверх
    каждый непарный столбец и по убыванию сверху
    вниз каждый парный столбец
    :return: None
    """

    m = int(input("Введите размер матрицы"))
    m_na_m = [[rnd.randint(1, 50) for _ in range(m)] for __ in range(m)]
    # считаем сумму столбцов
    m_list = [0 for _ in range(m)]
    for column_ in range(m):
        for raw_ in range(m):
            m_list[column_] += m_na_m[raw_][column_]
    m_na_m.append(m_list)

    print("Предварительная матрица")
    visio_matrix(m_na_m)
    # сортируем столбцы по сумме
    for j in range(m):
        for i in range(m - 1):
            if m_na_m[m][i] > m_na_m[m][i + 1]:
                m_na_m[m][i], m_na_m[m][i + 1] = m_na_m[m][i + 1], m_na_m[m][i]
                for __ in range(m):
                    m_na_m[__][i], m_na_m[__][i + 1] = m_na_m[__][i + 1], \
                                                     m_na_m[__][i]

    for __ in range(m):
        for j in range(m - 1):
            for i in range(m):
                # вычисляем четный или нечетный
                if i % 2 == 0:
                    if m_na_m[j][i] < m_na_m[j + 1][i]:
                        m_na_m[j][i], m_na_m[j + 1][i] = \
                            m_na_m[j + 1][i], m_na_m[j][i]
                else:
                    if m_na_m[j][i] > m_na_m[j + 1][i]:
                        m_na_m[j][i], m_na_m[j + 1][i] = \
                            m_na_m[j + 1][i], m_na_m[j][i]

    print("Отсортированная матрица")
    visio_matrix(m_na_m)


if __name__ == "__main__":

    do_sorted_arr()
