from my_module import visioner_array
from random import randint


class Ships(): # , palub, start_point
    povorot = randint(2)
    def set_attribut(self, name='Однотрубный', palub=2, k_vo=4):
        self.name = name
        self.palub = palub
        self.k_vo = k_vo

    def draw(self):
        self.shipp = ["██" for _ in range(self.palub)]
        self.ship_around = [["--" for _ in range(self.palub + 2)] for __ in
                            range(3)]
        # return self.shipp

    def show_me(self):
        print("название:", self.name)
        print("колич кораблей:", self.k_vo)
        print("колич труб:", self.palub, self.shipp)
        print("okrujenie :", self.ship_around)


class Board:

    razmer_morya = 10
    verhn_liniya = ['A', 'B', 'C', 'D', 'I', 'F', 'G', 'H', 'I', 'J']
    bokovaya_liniya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self):

        self.matrix_pole = [["░░" for __ in range(self.razmer_morya + 1)]
                            for _ in range(self.razmer_morya + 1)]

        for i in range(self.razmer_morya):
            self.matrix_pole[0][0] = ""
            self.matrix_pole[0][i+1] = self.verhn_liniya[i]
            self.matrix_pole[i+1][0] = str(self.bokovaya_liniya[i])

    def insert_ship(self, start_pos="5_1", gor_ver=1):
        """
        :param start_pos: "x_y"
        :param gor_ver: 1 - горизонтальное положение
                        2 - вертикальное положение
        """
        a = start_pos.split('_')
        x = int(a[1])
        y = int(a[0])
        for _ in range(ship_1.palub):
            self.matrix_pole[y + _][x] = ship_1.shipp[_]



    def show_board(self):
        print("Матрица поля")
        visioner_array(self.matrix_pole)


ship_1 = Ships()
ship_1.set_attribut('Четырёхтрубный', 4, 1)

ship_1.draw()
ship_1.show_me()
ship_2 = Ships()
ship_2.set_attribut('Трёхтрубный', 3, 2)
ship_2.draw()
ship_2.show_me()
ship_3 = Ships()
ship_3.set_attribut('Однотрубный', 1, 4)
ship_3.draw()
ship_3.show_me()

more = Board()
more.insert_ship()
more.show_board()
