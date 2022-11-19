import random as rd


new_dictionary = {i: rd.randint(1, 3) for i in range(1, 21)}
print("Сгенерированный словарь\n", new_dictionary)

rez_dict = 1
for i in new_dictionary.values():
    rez_dict *= i
print("Результат умножения значений\n", rez_dict)
