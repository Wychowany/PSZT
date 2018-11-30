

class Warehouse:
    matrix = None
    WIDTH = 100
    HEIGHT = 100
    entrance = None

    def __init__(self):
        self.matrix = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.init_matrix()

    def init_matrix(self):
        for j in range(self.WIDTH):
            for i in range(self.HEIGHT):
                self.matrix[i][j] = -1

    def set_entrance(self, point):
        self.entrance = point

