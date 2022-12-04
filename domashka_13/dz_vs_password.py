import string


def proverka(par, uslovie):
    for i in par:
        if i in uslovie:
            return par
        else:
            continue
    return None


def dekorator_pass(func):
    def wrapper():
        lenght_txt = "Пароль должен быть не менее 8ми символов в длину."
        space_txt = "Пароль не должен содержать пробельных символов и табуляций"
        digit_txt = "Пароль должен содержать минимум одну цифру"
        symbol_txt = "Пароль должен содержать минимум один спец символ"

        print(f'{"-" * 82}\n'
              f'|{space_txt:^80}|\n'
              f'|{lenght_txt:^80}|\n'
              f'|{digit_txt:^80}|\n'
              f'|{symbol_txt:^80}|\n'
              f'{"-" * 82}')

        while True:

            f = func()
            if f is None:
                print(f'{space_txt:^80}')
            else:
                if proverka(f, string.punctuation) is None:
                    print(f'{symbol_txt:^80}')
                if proverka(f, string.digits) is None:
                    print(f'{digit_txt:^80}')
                if len(f) < 8:
                    print(f'{lenght_txt:^80}')
                if proverka(f, string.punctuation) is not None and proverka(
                        f, string.digits) is not None and len(f) >= 8:
                    print(f'{"Пароль принят":^80}')
                    return f
    return wrapper


@dekorator_pass
def parol():
    """
    Функция запрашивает пароль и определяет пробельные символы
    :return: bool or str
    """
    z = str(input('Введите пароль :'))
    for i in z:
        if i in string.whitespace or i == " ":
            return None
    return z


if __name__ == "__main__":

    print(parol())
