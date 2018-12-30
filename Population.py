import Individual


class Population:

    individuals = None

    def __init__(self, matrix) -> None:
        super().__init__()
        self.individuals = [Individual.Individual(matrix) for _ in range(100)]
