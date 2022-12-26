from my_module import visioner_list
from random import randint
class Ship():
    palubi = 1
    orientation = 1
    point_ship = []
    point_nearby = []
    ship_ok = 1

    def __init__(self, palubi, orientation, start_coord):
        self.palubi = palubi
        self.orientation = orientation
        self.point_ship = []
        self.point_nearby = []
        self.ship_ok = 1

    pass

class Board:
    letters = ['ABCDEFJKLM']
    coord_field = []
    #  draw empty
    def draw_coord_empty_field(self):
        for i in range(1, 11): # x-stroka
            for j in range(1, 11): # y-stolbec
                x_y = str(i) + ';' + str(j)
                self.coord_field.append(x_y)
        return self.coord_field

    # создаю корабль с произвольными начальными координатами
    rand_start_coord = str(randint(1, 11)) + ';' + str(randint(1, 11))
    print(rand_start_coord)
    for i in range(4,0,-1):  # палубность 4-1
        for j in range(1,5): # количество кораблей

            


bd = Board()
visioner_list(bd.draw_coord_empty_field())


