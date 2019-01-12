import Cargo
import random

class Individual:

    topLeftCorner_X = None
    topLeftCorner_Y = None
    isVisible = None
    Cargo = None

    def __init__(self,x):
        super().__init__()
        isVisible = choice(True, False)
        topLeftCorner_X = random(0, 100, 1)
        topLeftCorner_Y = random(0, 100, 1)
        if x == 1:
            Cargo = SmallSquare.SmallSquare()
        elif x == 2:
            Cargo = SmallRectangleHorizontal.SmallRectangleHorizontal()
        elif x == 3:
            Cargo = SmallRectangleVertical.SmallRectangleVertical()
        elif x == 4:
            Cargo = MediumSquare.MediumSquare()
        elif x == 5:
            Cargo = MediumRectangleHorizontal.MediumRectangleHorizontal()
        elif x == 6:
            Cargo = MediumRectangleVertical.MediumRectangleVertical()
        elif x == 7:
            Cargo = BigSquare.BigSquare()

    def isThereAPath(self, matrix):
        
        return self.findPath(self, matrix, self.topLeftCorner_X, self.topLeftCorner_Y)

    def findPath(self, matrix, x, y):
        if matrix[x][y] == -1:
            return True
        elif matrix[x-1][y] == 0:
            top = self.findPath(matrix,x-1,y)
            if top == True:
                return top
        elif matrix[x][y+1] == 0:
            right = self.findPath(matrix,x,y+1)
            if right == True:
                return right
        elif matrix[x+1][y] == 0:
            down = self.findPath(matrix,x+1,y)
            if down == True:
                return down
        elif matrix[x][y-1] == 0:
            left = self.findPath(matrix,x,y-1)
            if left == True:
                return left
        return False

    def isFullyInBounds(self,matrix,height,width):
        for i in range(topLeftCorner_Y, topLeftCorner_Y + Cargo.height):
            for j in range(topLeftCorner_X, topLeftCorner_X + Cargo.width):
                if matrix[i][j] < 0:
                    return False

        return True

    def mutate(self):
        a = random(1, 11, 1)
        if a == 1:
            b = random(1, 4, 1)
            if b == 1:
                self.isVisible = choice(True, False)
            elif b == 2:
                self.topLeftCorner_X = random(0, 100, 1)
            else:
                self.topLeftCorner_Y = random(0, 100, 1)