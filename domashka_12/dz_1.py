import random as rd


def test_sum_1(list_1, var_1):
    """
    :param list_1: list or generator
    :param var_1: var for if
    :return: Bool
    """
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if i == j:  # Исключает сложение самого с собой
                break
            if list_1[i] + list_1[j] == var_1:
                return True
    return False


print(test_sum_1(range(1, 11000, 100), 502))
print(test_sum_1(range(1, 11, 2), 7))  # числа не четные сумма четная
print(test_sum_1((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 19))

listik = []
for k in range(1, 10):
    listik.append(rd.randint(1, 1 * 10 ** 1000))
print(test_sum_1(listik, 19))
