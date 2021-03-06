#!/usr/bin/bash
# -*- coding: utf-8 -*
import Cargo
import random

class Individual:

    topLeftCorner_X = None
    topLeftCorner_Y = None
    isVisible = None
    cargo = None

    def __init__(self,x):
        #super().__init__()
        self.isVisible = random.choice([True, False])
        self.topLeftCorner_X = random.randrange(0, 100, 1)
        self.topLeftCorner_Y = random.randrange(0, 100, 1)
        if x == 1:
            self.cargo = Cargo.Cargo(1,1)
        elif x == 2:
            self.cargo = Cargo.Cargo(1,2)
        elif x == 3:
            self.cargo = Cargo.Cargo(2,1)
        elif x == 4:
            self.cargo = Cargo.Cargo(2,2)
        elif x == 5:
            self.cargo = Cargo.Cargo(2,3)
        elif x == 6:
            self.cargo = Cargo.Cargo(3,2)
        elif x == 7:
            self.cargo = Cargo.Cargo(5,5)


    #nie dziala
    #szkielet, mozna zmienic koncepcje, trzeba poprawic zeby nie wykraczac poza zakres, lub zmienic ladunek tak zeby nie mogl wykraczac poza zakres              
    def registerCargo(self, warehouse):
        for i in range(self.topLeftCorner_Y, self.topLeftCorner_Y + self.cargo.height):
            for j in range(self.topLeftCorner_X,self.topLeftCorner_X + self.cargo.width):
                if i >= 0 and i <= 100 and j >= 0 and j <= 100:
                    if warehouse[i][j] <= -3:
                        warehouse[i][j] = warehouse[i][j] - 1
                    elif warehouse[i][j] >= 0:
                        warehouse[i][j] = warehouse[i][j] + 1

    def isThereAPath(self, matrix):

        result = False
        
        for i in range(self.topLeftCorner_X, self.topLeftCorner_X + self.cargo.width, 1):
            result = self.findPath(matrix, self.topLeftCorner_Y, i)
            if result == True:
                return True

            if self.cargo.height > 1:
                result = self.findPath(matrix, self.topLeftCorner_Y + self.cargo.height -1, i)
                if result == True:
                    return True
        
        if self.cargo.height > 1:
            for i in range(self.topLeftCorner_Y, self.topLeftCorner_Y + self.cargo.height, 1):
                result = self.findPath(matrix, i, self.topLeftCorner_X)
                if result == True:
                    return True

                if self.cargo.width > 1:
                    result = self.findPath(matrix, i, self.topLeftCorner_X + self.cargo.width - 1)
                    if result == True:
                        return True

    def findPath(self, matrix, x, y):
        if matrix[x][y] == -1:
            return True
        elif matrix[x-1][y] == 0:
            top = self.findPath(matrix, x-1, y)
            if top == True:
                return top
        elif matrix[x][y+1] == 0:
            right = self.findPath(matrix, x, y+1)
            if right == True:
                return right
        elif matrix[x+1][y] == 0:
            down = self.findPath(matrix, x+1, y)
            if down == True:
                return down
        elif matrix[x][y-1] == 0:
            left = self.findPath(matrix, x, y-1)
            if left == True:
                return left
        return False

    def isFullyInBounds(self, matrix, height, width):
        for i in range(self.topLeftCorner_Y, self.topLeftCorner_Y + self.cargo.height):
            for j in range(self.topLeftCorner_X, self.topLeftCorner_X + self.cargo.width):
                if i < height and j < width:
                    if matrix[i][j] < 0:
                        return False
        return True

    def mutate(self):
        a = random.randrange(1, 11, 1)
        if a == 1:
            b = random.randrange(1, 4, 1)
            if b == 1:
                self.isVisible = random.choice([True, False])
            elif b == 2:
                self.topLeftCorner_X = random.randrange(0, 100, 1)
            else:
                self.topLeftCorner_Y = random.randrange(0, 100, 1)