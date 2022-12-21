def set_glue():
    """Складывает два числа"""
    a = input("a: ")
    b = input("b: ")

    try:
        print("a + b", a + b)
    except TypeError:
        print("a + b = ", str(a) + str(b))


set_glue()

