god = input("Enter a year to check 1900 -- 1000000  :")

if not god.isdigit():  # на случай, если ввели буквы
    print("The year does not meet the criteria, please enter an integer")
else:
    god = int(god)
    if 1900 < god < 1000000:
        if god % 4 == 0:
            if god % 400 != 0 and god % 100 == 0:
                print(god, "is not leep year ")
            else:
                print(god, "is leep year")
        else:
            print(god, "is not leap year")
    else:
        print("The range does not meet the conditions ")
