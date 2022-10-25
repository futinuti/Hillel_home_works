my_password = "password"
password = str(input("Input password :"))

if password not in my_password:
    print("У доступі отказано ")
else:
    print("Пароль прийнято")
