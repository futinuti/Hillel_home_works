input_str = input("Введіть строку :\n")
input_char = input("Введіть символ для пошуку :\n")
i = 0
cnt = 0
while input_str.find(input_char, i) > 0:
    print(input_str.find(input_char, i), end="; ")
    i = input_str.find(input_char, i) + 1
    cnt += 1
print("Найденных символов :", cnt)
