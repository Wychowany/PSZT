#!/usr/bin/bash
# -*- coding: utf-8 -*
import Individual
import copy


class Population:

    individuals = None
    objectiveFunctionValue = None
    warehouse = None

    def __init__(self, x, matrix):
        #super().__init__()
        self.individuals = [Individual.Individual(x[i]) for i in range(100)]
        self.objectiveFunctionValue = 0
        self.warehouse = copy.deepcopy(matrix)

    '''
        Objective function defines how little of warehouse's space is free
        Base value: 0
        Added value: 1 for every possision with an item
        Penalty value: 5 for every overlaping item in given possition
        Penalty value: 20 if a item is not fully in the warehouse
        Penalty value: 50 if there is no path to the item
    '''
    def evaluateObjectiveFunction(self, height, width):
        self.objectiveFunctionValue = 0

        for y in range(width):
            for x in range(height):
                if self.warehouse[x][y] >= 0:
                    self.objectiveFunctionValue += (self.warehouse[x][y] - 1) * 5 + 1

        for item in self.individuals:
            if item.isFullyInBounds(self.warehouse,height,width) == False:
                self.objectiveFunctionValue += 20

            #if item.isThereAPath(self.warehouse)== False:
                #self.objectiveFunctionValue += 50

    def putCargosIntoWarehouse(self):
        for item in self.individuals:
            item.registerCargo(self.warehouse)

    def debug_warehouse_shape(self):
        counter = 0
        for x in range(101):
            y = 0
            while y < 101:
                if self.warehouse[x][y] == 0:
                    print("x", end=" ")

                elif self.warehouse[x][y] >= 10:
                    print("o", end=" ")
                elif self.warehouse[x][y] > 0:
                    print(self.warehouse[x][y], end=" ")

                elif self.warehouse[x][y] == -1:
                    print("_", end=" ")
                elif self.warehouse[x][y] == -3:
                    print("a", end=" ")
                elif self.warehouse[x][y] <= -4:
                    print("b", end=" ")
                else:
                    print(" ", end=" ")
                y += 1
            print("")
        print(self.objectiveFunctionValue)
