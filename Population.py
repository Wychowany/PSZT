#!/usr/bin/bash
# -*- coding: utf-8 -*
import Individual


class Population:

    individuals = None
    objectiveFunctionValue = None
    warehouse = None

    def __init__(self, x, matrix):
        #super().__init__()
        self.individuals = [Individual.Individual(x[i]) for i in range(100)]
        self.objectiveFunctionValue = 0
        self.warehouse = matrix

    '''
        Objective function defines how little of warehouse's space is free
        Base value: 0
        Added value: 1 for every possision with an item
        Penalty value: 5 for every overlaping item in given possition
        Penalty value: 20 if a item is not fully in the warehouse
        Penalty value: 50 if there is no path to the item
    '''
    def evaluateObjectiveFunction(self, height, width):
        objectiveFunctionValue = 0
        for y in range(width):
            for x in range(height):
                objectiveFunctionValue += (self.warehouse[x][y] - 1) * 5 + 1

        for item in self.individuals:
            if item.isFullyInBounds == False:
                objectiveFunctionValue += 20

            if item.isThereAPath == False:
                objectiveFunctionValue += 50

    def putCargosIntoWarehouse(self):
        for item in self.individuals:
            item.registerCargo(self.warehouse)