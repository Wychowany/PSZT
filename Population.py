import Individual


class Population:

    individuals = None
    objectiveFunctionValue = None
    warehouse = None

    def __init__(self, x, matrix):
        super().__init__()
        if len(x) > 0:# ze wzgledu na reprodukcje, bo nie mozna przeciazyc konstruktora, SUPER JEZYK XD
            self.individuals = [Individual.Individual(x[i]) for i in range(100)]
        objectiveFunctionValue = 0
        warehouse = matrix

    '''
        Objective function defines how little of warehouse's space is free
        Base value: 0
        Added value: 1 for every possision with a cargo
        Penalty value: 5 for every overlaping cargo in given possition
        Penalty value: 20 if a cargo is not fully in the warehouse
        Penalty value: 50 if there is no path to the cargo
    '''
    def evaluateObjectiveFunction(self, height, width):
        objectiveFunctionValue = 0
        for y in range(width):
            for x in range(height):
                objectiveFunctionValue += (self.warehouse[x][y] - 1) * 5 + 1

        for cargo in self.individuals:
            if cargo.isFullyInBounds == False:
                objectiveFunctionValue += 20

            if cargo.isThereAPath == False:
                objectiveFunctionValue += 50
'''
    def putCargosIntoWarehouse(self):
        for cargo in self.individuals
            self.registerCargo(cargo)

    szkielet, można zmienic koncepcje, trzeba poprawic zeby nie wykraczac poza zakres, lub zmienic ladunek tak zeby nie mogl wykraczac poza zakres              
    def registerCargo(self, cargo)
        for i in range(cargo.topLeftCorner_Y,cargo.topLeftCorner_Y + cargo.height)
            for j in range(cargo.topLeftCorner_X,cargo.topLeftCorner_X + cargo.width)
                if self.warehouse[i][j] <= -3:
                    self.warehouse[i][j] = self.warehouse[i][j] - 1
                elif self.warehouse[i][j] >= 0:
                    self.warehouse[i][j] = self.warehouse[i][j] + 1
'''