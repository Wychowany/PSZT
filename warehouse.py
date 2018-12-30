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
                self.matrix[i][j] = State.State.OUT_OF_BOUNDS

    def set_way_on_matrix_when_moving_up(self):
        for i in range(5):
            self.matrix[self.index_x - i][self.index_y] = State.State.WALL

        self.index_x -= 5

    def set_way_on_matrix_when_moving_down(self):
        for i in range(5):
            self.matrix[self.index_x + i][self.index_y] = State.State.WALL
        self.index_x += 5

    def set_way_on_matrix_when_moving_left(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y - i] = State.State.WALL
        self.index_y -= 5

    def set_way_on_matrix_when_moving_right(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y + i] = State.State.WALL
        self.index_y += 5

    def fill_warehouse(self):
        self.fill_field(49, 50) # hardcoded, wystarczy podać jakiś punkt wewnątrz magazynu
        # self.debug_warehouse_shape()

    def fill_field(self, x, y):
        if x > 99 or y > 99 or x < 0 or y < 0 or self.matrix[x][y] == State.State.WALL \
                or self.matrix[x][y] == State.State.FREE_SPACE:
            return
        elif self.matrix[x][y] == State.State.OUT_OF_BOUNDS:
            self.matrix[x][y] = State.State.FREE_SPACE

        self.fill_field(x-1, y)
        self.fill_field(x, y+1)
        self.fill_field(x+1, y)
        self.fill_field(x, y-1)



    def debug_warehouse_shape(self):
        counter = 0
        for x in range(self.HEIGHT):
            y = 0
            while y < self.WIDTH:
                if self.matrix[x][y] == State.State.FREE_SPACE: # natrafiamy na ściane
                    counter += 1
                    print("x", end='')
                else:
                    print(" ", end='')
                y += 1
            print("")
        print(counter)



