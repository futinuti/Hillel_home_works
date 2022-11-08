# spisok="Это давно установ,ленный факт,,   --   что!! читателей будет отвлекаться на     удобчтмое сдержние страницы."

spisok = input("Введите предложение")
lst_1 = spisok.split(" ")
print(lst_1)
# убираю знаки препинания
cnt = 0
for i in lst_1:
    if not i.isalpha():
        spisok_1 = list(i)
        for j in spisok_1:
            if not j.isalpha():
                for k in range(spisok_1.count(j)):
                    spisok_1.remove(j)
        lst_1.pop(cnt)
        lst_1.insert(cnt, "".join(spisok_1))
    cnt += 1

# убираю пустые строки
for i in range(lst_1.count("")):
    lst_1.remove("")

# Сортировка
lst_1.sort()

# Таблица
print("_" * 43)
print(f'|{"Слово":^30}|{"Индекс":^10}|')
print("-" * 43)

for i in range(len(lst_1)):
    print(f'|{lst_1[i]:^30}|{i:^10}|')

print("-" * 43)
print(f'|{"К-во слов":^30}|{len(lst_1):^10}|')
print("-" * 43)
