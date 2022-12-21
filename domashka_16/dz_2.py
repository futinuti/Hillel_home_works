def dict_handler(dict_in, key_in, value_in="default"):
    try:

        value_in = dict_in[key_in]

        print("Без ошибки")

    except KeyError:
        dict_in[key_in] = value_in
        print("Ошибка ключа")

    except TypeError:
        print("Изменяемые типы данных не могут быть ключём")
        key_in = None

    finally:
        return key_in, value_in


dict_out = {"a": 65}

print('"Неправильный ключ"')
print("Ключ :{0[0]}, Значение :{0[1]}".format(
    dict_handler(dict_out, dict_out, "b")
    ))
print()
print('"Отсутствует ключ"')
print("Ключ :{0[0]}, Значение :{0[1]}".format(
    dict_handler(dict_out, "b")
    ))
print()
print('"Без ошибки"')
print("Ключ :{0[0]}, Значение :{0[1]}".format(
    dict_handler(dict_out, "a")
    ))
