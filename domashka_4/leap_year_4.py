god = input("Enter a year to check 1900 -- 1 000 000  :")

if not god.isdigit():  # на случай, если ввели буквы
    print("The year does not meet the criteria, please enter an integer")
else:
    god = int(god)
    if god < 1900 or god > 1000000:
        print("The range does not meet the conditions ")
    else:
        if god % 4 == 0 or god % 400 == 0 or god % 100 == 0:
            print(god, "is leap year ")
        else:
            print(god, "is not leap year")
