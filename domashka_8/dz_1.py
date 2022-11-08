lst_1 = list(range(10, 251))
# print("Исходный список\n", lst_1)
for i in lst_1:
    if i % 20 == 0:
        lst_1.remove(i)
print("Результат\n", lst_1)
