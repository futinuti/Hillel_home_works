def set_glue():
    """Складывает два числа"""
    a = input("a: ")
    b = input("b: ")

    try:
        print("a + b =", int(a) + int(b))
    except ValueError:
        print("a + b = ", str(a) + str(b))

set_glue()

