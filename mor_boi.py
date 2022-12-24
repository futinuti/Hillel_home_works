from my_module import visioner_array
class Ship():

    colichestvo_palub = 1
    name_ship = "Simply Ship"
    var_pov = 1
    col_ships = 4
    koord_ship = []

    def name(self, n):
        self.name_ship = n

    def palubi(self, pal):
        self.colichestvo_palub = pal

    def flot(self, f):
        self.col_ships = f

    def show_me(self):
        print("название:", self.name_ship)
        print("колич кораблей:", self.col_ships)
        print("колич труб:", self.colichestvo_palub)


class Board():

    razmer_morya = 10
    verhn_liniya = ['A', 'B', 'C', 'D', 'I', 'F', 'G', 'H', 'I', 'J']
    bokovaya_liniya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def __init__(self):

        self.matrix_pole = [[" " for i in range(self.razmer_morya + 1)]
                       for _ in range(self.razmer_morya + 1)]

        for i in range(self.razmer_morya):
            self.matrix_pole[0][0] = ""
            self.matrix_pole[0][i+1] = self.verhn_liniya[i]
            self.matrix_pole[i+1][0] = self.bokovaya_liniya[i]

    def show_board(self):
        print("Матрица поля")
        visioner_array(self.matrix_pole)


pervi_korabl = Ship()
vtoroi_korabl = Ship()
vtoroi_korabl.palubi(4)

more = Board()
more.show_board()
