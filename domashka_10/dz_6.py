def clean_empty_str(spisok):
    """ remove blank lines """
    for i in range(spisok.count("")):
        spisok.remove("")
    return spisok


def max_quantity_word(dictionary):
    # min_dict = {}
    for keyw, val in dictionary.items():
        if val == max(dictionary.values()):
            print('Наиболее встречается "', keyw, '", встречается ', val, 'раз')
    """  if val == min(dictionary.values()):
            min_dict[keyw] = val
    print('Наименее встречается "', list(min_dict.keys()), '", встречается ',
          min(dictionary.values()), 'раз')"""


stih = (
        "Любіть Україну, як сонце любіть, " +
        'як вітер, і трави, і води... ' +
        "В годину щасливу і в радості мить, " +
        "любіть у годину негоди. " +
        " — " +
        "Любіть Україну у сні й наяву, " +
        "вишневу свою Україну, " +
        "красу її, вічно живу і нову, " +
        "і мову її солов'їну. " +
        " — " +
        "Без неї — ніщо ми, як порох і дим, " +
        "розвіяний в полі вітрами... " +
        "Любіть Україну всім серцем своїм " +
        "і всіми своїми ділами. ")

list_1 = stih.split()
cleaned_list = []

for word in list_1:
    cleaned_word = ''.join(char for char in word
                           if char.isalnum() and char.isalpha())
    cleaned_list.append(cleaned_word)

clean_empty_str(cleaned_list)
# print(cleaned_list)
rez_dictionary = {}

for key in cleaned_list:
    counter = 0
    for letter in cleaned_list:
        if key == letter:
            counter += 1
    rez_dictionary[key] = counter

print(rez_dictionary)
max_quantity_word(rez_dictionary)
