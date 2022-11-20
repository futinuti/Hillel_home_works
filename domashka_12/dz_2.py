kvadrat = map(lambda x, y=2: x ** y, range(1, 8))
print(list(kvadrat))  # берет только 'х'

kvadrat = map(lambda x, y=2: x ** y, range(11, 18), range(1, 8))
print(list(kvadrat))  # берет и 'x', и 'y'
