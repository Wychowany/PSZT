#!/usr/bin/bash
# -*- coding: utf-8 -*

class Warehouse:

    matrix = None
    WIDTH = 101 #zrobilem na razie 101 x 101, bo nie chcialem bawic w ograniczanie funkcji do poruszania sie
    HEIGHT = 101   #zeby uniknac wychodzenia poza zakres
    entrance = None
    index_x = 50
    index_y = 50
    first = True

    def __init__(self):
        self.matrix = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.init_matrix()

    def init_matrix(self):
        for j in range(self.WIDTH):
            for i in range(self.HEIGHT):
                self.matrix[i][j] = -3

    def set_way_on_matrix_when_moving_up(self):
        for i in range(5):
            self.matrix[self.index_x - i][self.index_y] = -2

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = -1
            self.first = False
        self.index_x -= 5

    def set_way_on_matrix_when_moving_down(self):
        for i in range(5):
            self.matrix[self.index_x + i][self.index_y] = -2

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = -1
            self.first = False

        self.index_x += 5

    def set_way_on_matrix_when_moving_left(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y - i] = -2

            if self.first is True:
                self.matrix[self.index_x][self.index_y] = -1
                self.first = False

        self.index_y -= 5

    def set_way_on_matrix_when_moving_right(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y + i] = -2

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = -1
            self.first = False

        self.index_y += 5

    def fill_warehouse(self):
        #self.fill_field(49, 50)  hardcoded, wystarczy podac jakis punkt wewnatrz magazynu
        self.fill_field(49, 50)
        self.debug_warehouse_shape()

    #zrobilem iteracyjnie, wydaje sie bardziej przejrzyste
    def fill_field(self, x, y):
       if x > 99 or y > 99 or x < 0 or y < 0 or self.matrix[x][y] == -2 \
               or self.matrix[x][y] == 0 or self.matrix[x][y] == -1:
           return
       elif self.matrix[x][y] == -3:
           self.matrix[x][y] = 0

       self.fill_field(x-1, y)
       self.fill_field(x, y+1)
       self.fill_field(x+1, y)
       self.fill_field(x, y-1)



    def debug_warehouse_shape(self):
        counter = 0
        for x in range(self.HEIGHT):
            y = 0
            while y < self.WIDTH:
                if self.matrix[x][y] == 0:
                    counter += 1
                    print("x", end='')
                else:
                    print(" ", end='')
                y += 1
            print("")
        print(counter)