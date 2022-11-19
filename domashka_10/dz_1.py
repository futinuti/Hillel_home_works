dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
'''
# Обьединяем с помощью цикла for
merged_dictionary = {}
# Перебираем пары словарей поочередно с помощью метода .items()
for key, value in dictionary_1.items():
    merged_dictionary[key] = value
for key, value in dictionary_2.items():
    merged_dictionary[key] = value
print(merged_dictionary, "__1__")

# Обьединяем с помощью метода .update()
merged_dictionary = {}
merged_dictionary.update(dictionary_1)
merged_dictionary.update(dictionary_2)
print(merged_dictionary, "__2__")

# Обьединяем с помощью оператора ( ** )
merged_dictionary = {**dictionary_1, **dictionary_2}
print(merged_dictionary, "__3__")
'''
# Обьединяем с помощью оператора ( | ) в версии  3.9
merged_dictionary = dictionary_1 | dictionary_2
print(merged_dictionary, "__4__")
