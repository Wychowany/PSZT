#!/usr/bin/bash
# -*- coding: utf-8 -*
import Individual


class Population:

    individuals = None
    objectiveFunctionValue = None
    warehouse = None
    OVERLAPPING_PENALTY = 5
    OUT_OF_BOUNDS_PENALTY = 20
    NO_PATH_PENALTY = 50

    def __init__(self, x, matrix):
        #super().__init__()
        self.individuals = [Individual.Individual(x[i]) for i in range(100)]
        self.objectiveFunctionValue = 0
        self.warehouse = matrix

    '''
        Objective function defines how little of warehouse's space is free
        Base value: 0
        Added value: 1 for every possision without an item
        Penalty value: 5 for every overlaping item in given possition
        Penalty value: 20 if a item is not fully in the warehouse
        Penalty value: 50 if there is no path to the item
    '''
    def evaluateObjectiveFunction(self, height, width):
        objectiveFunctionValue = 0
        for y in range(width):
            for x in range(height):
                if self.warehouse[x][y] == 0:
                    objectiveFunctionValue += 1
                elif self.warehouse[x][y] > 1:
                    objectiveFunctionValue += (self.warehouse[x][y] - 1) * self.OVERLAPPING_PENALTY

        for item in self.individuals:
            if item.isFullyInBounds == False:
                objectiveFunctionValue += self.OUT_OF_BOUNDS_PENALTY

            if item.isThereAPath == False:
                objectiveFunctionValue += self.NO_PATH_PENALTY

    def putCargosIntoWarehouse(self):
        for item in self.individuals:
            item.registerCargo(self.warehouse)