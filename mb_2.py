# from my_module import visioner_list
from random import randrange


class Ship:
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

        while self.ship_ok == 0:
            if orientation == 0 and int(start_coord[0]) + palubi <= 9:
                self.ship_ok = 1
                for i in range(1, palubi+1):
                    gorizont = i + int(start_coord[0])
                    vertical = int(start_coord[2])
                    self.point_ship.append(str(gorizont) + ';' + str(vertical))
            if orientation == 1 and int(start_coord[2]) + palubi <= 9:
                self.ship_ok = 1
                for i in range(1, palubi+1):
                    gorizont = int(start_coord[0])
                    vertical = i + int(start_coord[2])
                    self.point_ship.append(str(gorizont) + ';' + str(vertical))
            else:
                self.ship_ok = 0
                break

            print(self.ship_ok, orientation)
            print(self.point_ship)

class Board:
    letters = ['ABCDEFJKLM']
    coord_field = []
    orient = 1
    #  draw empty

    def draw_coord_empty_field(self):
        for i in range(10):  # x-stroka
            for j in range(10):  # y-stolbec
                x_y = str(i) + ';' + str(j)
                self.coord_field.append(x_y)
        return self.coord_field


    # print(rand_start_coord)
    for i in range(5, 0, -1):  # палубность 4-1
        for j in range(5 - i):  # количество кораблей
            while True:
                orient = randrange(2)  # произвольная ориентация
                # создаю корабль с произвольными начальными координатами
                rand_start_coord = str(randrange(10)) + ';' + str(randrange(10))
                ship = Ship(i, orient, rand_start_coord)
                if ship.ship_ok == 1:
                    break


bd = Board()
# visioner_list(bd.draw_coord_empty_field())
