while True:

    input_str = input("Введіть два слова через пробіл :\n")
    str_splited = input_str.split(" ")

    if len(str_splited) != 2 or not str_splited[0].isalpha() or not str_splited[1].isalpha():
        print("Перевiрте введенi даннi")
    else:
        break

print(str_splited[0][::-1].capitalize(), str_splited[1][::-1].capitalize())
