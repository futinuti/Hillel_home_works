#
# f = open('exmp.txt', 'w')
# i = "true"
# while i != "":
#     i = input("Введите строку:")
#     f.write(i + "\n")
# f.close()

with open('exmp.txt', 'w') as f:
    i = "true"
    while i != "":
        i = input("Введите строку:")
        f.write(i + "\n")
