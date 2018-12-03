import State

class Warehouse:
    matrix = None
    WIDTH = 100
    HEIGHT = 100
    entrance = None
    index_x = 50
    index_y = 50

    def __init__(self):
        self.matrix = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.init_matrix()

    def init_matrix(self):
        for j in range(self.WIDTH):
            for i in range(self.HEIGHT):
                self.matrix[i][j] = -1

    def set_way_on_matrix_when_moving_up(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y - i] = 0

        self.index_y -= 5

    def set_way_on_matrix_when_moving_down(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y + i] = 0
        self.index_y += 5

    def set_way_on_matrix_when_moving_left(self):
        for i in range(5):
            self.matrix[self.index_x - i][self.index_y] = 0
        self.index_x += 5

    def set_way_on_matrix_when_moving_right(self):
        for i in range(5):
            self.matrix[self.index_x + i][self.index_y] = 0
        self.index_x -= 5



