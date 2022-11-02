while True:
    row = input("Input number from 3 to 9:")

    if row.isdigit():
        row = int(row)
        if not 3 <= row <= 9:
            print("Not correct")
        else:
            break
    else:
        print("Not correct")

stroka_1 = "123456789"
width_pyramid = row * 2 + 1
while True:
    variant = str(input("вариант выравнивания \n"
                        "1 - лево,\n"
                        "2 - центр,\n"
                        "3 - право,\n"
                        "любая другая - выход"))
    if variant == "1":
        print(stroka_1[0].ljust(width_pyramid, "*"))
        for i in range(1, row):
            a = stroka_1[0:i + 1] + stroka_1[i - 1::-1]
            print(a.ljust(width_pyramid, "*"))

    elif variant == "2":
        print(stroka_1[0].center(width_pyramid, "_"))
        for i in range(1, row):
            a = stroka_1[0:i+1] + stroka_1[i-1::-1]
            print(a.center(width_pyramid, "_"))

    elif variant == "3":
        print(stroka_1[0].rjust(width_pyramid, "_"))
        for i in range(1, row):
            a = stroka_1[0:i+1] + stroka_1[i-1::-1]
            print(a.rjust(width_pyramid, "_"))
    else:
        break
