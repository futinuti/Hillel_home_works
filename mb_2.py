from my_module import visioner_array
from random import randrange


class Ship:
    """Класс Ship создает корабли с заданными свойствами
    палубность (1-4) поступающий на вход при создании
    ориентация (0 - верт., 1 - гориз.) поступающий на вход при создании
    начальные координаты корабля, поступающий на вход при создании
    список координат корабля
    список координат вокруг корабля"""
    palubi = 1
    orientation = 1
    point_ship = []
    point_nearby = []
    ship_ok = 1
    start_coord = ''

    def __init__(self, palubi, orientation, start_coord):
        self.palubi = palubi
        self.orientation = orientation
        self.point_ship = []
        self.point_nearby = []
        self.ship_ok = 0
        self.start_coord = start_coord

        # проверка на то что корабль влазит в игровое поле
        # и создание координат корабля, коорд. рядом с кораблем
        while self.ship_ok == 0:

            if self.orientation == 0 and int(start_coord[0]) + palubi <= 9:
                self.ship_ok = 1
                for i in range(palubi):
                    gorizont = i + int(start_coord[0])
                    vertical = int(start_coord[2])
                    self.point_ship.append(str(gorizont) + ';' + str(vertical))
                    for k in range(3):
                        for j in range(palubi + 2):
                            self.point_nearby.append(
                                str(gorizont - 1 + j) + ';' +
                                str(vertical - 1 + k))
            elif self.orientation == 1 and int(start_coord[2]) + palubi <= 9:
                self.ship_ok = 1
                for i in range(palubi):
                    gorizont = int(start_coord[0])
                    vertical = i + int(start_coord[2])
                    self.point_ship.append(str(gorizont) + ';' + str(vertical))
                    for k in range(3):
                        for j in range(palubi + 2):
                            self.point_nearby.append(
                                str(gorizont - 1 + k) + ';' +
                                str(vertical - 1 + j))
            else:
                self.ship_ok = 0
                break


class Board:
    verhn_liniya = ['A', 'B', 'C', 'D', 'I', 'F', 'G', 'H', 'I', 'J']
    bokovaya_liniya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    orient = 1
    all_ships_in = []  # общее поле созданных кораблей с коорд рядом
    flot = []  # координаты всех кораблей
    matrix_pole = []

    def __init__(self):  # пустое поле
        self.matrix_pole = [["░░" for __ in range(11)]
                            for _ in range(11)]
        self.name_pole()

    def name_pole(self):
        for i in range(10):
            self.matrix_pole[0][0] = ""
            self.matrix_pole[0][i+1] = self.verhn_liniya[i]
            self.matrix_pole[i+1][0] = str(self.bokovaya_liniya[i])

    def n_ships(self):  # Создаём корабли
        for i in range(5, 0, -1):  # палубность 4-1
            for j in range(5 - i):  # количество кораблей
                while True:
                    orient = randrange(2)  # произвольная ориентация
                    # создаю корабль с произвольными начальными координатами
                    rand_start_coord = \
                        str(randrange(10)) + ';' + \
                        str(randrange(10))
                    ship = Ship(i, orient, rand_start_coord)
                    # переменная пересечения координат
                    krest = len(list(set(self.all_ships_in) & set(
                        ship.point_ship)))

                    if ship.ship_ok == 1 and krest == 0:
                        self.flot += ship.point_ship
                        self.all_ships_in += ship.point_nearby
                        break
        self.insert_ship()

    def insert_ship(self):
        for y in range(10):
            for x in range(10):
                m_p_coord = str(x) + ';' + str(y)
                if m_p_coord in self.flot:
                    self.matrix_pole[x+1][y+1] = '██'

    def draw_board(self):
        visioner_array(self.matrix_pole)


bd = Board()
bd.n_ships()
bd.draw_board()
